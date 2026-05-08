import pandas as pd
import sys, os
import json

CURRENT = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(CURRENT, "..")
sys.path.append(ROOT)

data = os.path.join(ROOT, "data","hderma_data.csv")
images_data = os.path.join(ROOT, "data","images_list.csv")
images = os.path.join(ROOT, "data",'images')

def input_data(filename:str,name:list, images:list, price:list, links:list):
    '''
    This function is used to input the data of the items that we have scraped from the website.'''
    try:
        data_template = {
            "name": name,
            "images": images,
            "price": price,
            "links": links
        }

        result = pd.DataFrame(data_template)
        result.to_csv(filename, index=False, encoding="utf-8-sig")
        return {
            "message": "Data has been successfully inserted into the CSV file."
        }

    except Exception as e:
        return {
            "error": str(e)
        }
    

def input_data_from_json(filename:str, data_queue:list):
    '''
    This function is used to input the data of the items that we have scraped from the website in JSON format.
    We will use this function to convert the data of the items from JSON format to CSV format and then insert it into the CSV file.
    '''
    try:
        data_template = {
            "name": [x.get("name") for x in data_queue],
            "images": [x.get("images") for x in data_queue],
            "price": [x.get("prices")[0] for x in data_queue],
            "links": [x.get("links") for x in data_queue]
        }

        result = pd.DataFrame(data_template)
        result.to_csv(filename, index=False, encoding="utf-8-sig")
        return {
            "message": "Data has been successfully inserted into the CSV file."
        }

    except Exception as e:
        return {
            "error": str(e)
        }


def list_images(images_data):
    '''
    This function is used to list the images of the items that we have scraped from the website.
    We will use this function to print the images of the items in JSON format
    '''
    image_storage = []
    try:
        if os.path.exists(images_data):
           data = os.listdir(images_data)
           for img in data:
               image_storage.append(img)
        return image_storage
    except Exception as e:
        return {
            "error": str(e)
        }
def insert_images(filename:str, images:list):
    '''
    This function is used to insert the images of the items that we have scraped from the website into a CSV file.
    We will use this function to convert the images of the items from a list to a CSV format and then insert it into the CSV file.
    '''
    try:
        data_template = {
            "images": images
        }

        result = pd.DataFrame(data_template)
        result.to_csv(filename, index=False, encoding="utf-8-sig")
        return {
            "message": "Images have been successfully inserted into the CSV file."
        }

    except Exception as e:
        return {
            "error": str(e)
        }
    
if __name__    == "__main__":
    print(list_images(images))
    print(insert_images(images_data, list_images(images)))

