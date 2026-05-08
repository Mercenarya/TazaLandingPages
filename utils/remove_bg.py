import os,sys

# Ép onnxruntime chỉ dùng CPU, chặn tìm kiếm CUDA
os.environ["ORT_LOGGING_LEVEL"] = "3" 
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

from PIL import Image
from rembg import remove, new_session

# cấu hình danh sách ảnh cần xử lí bg
CURRENT = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(CURRENT,"..")
sys.path.append(ROOT)

product_images = os.path.join(ROOT,'data','images')
for obj in os.listdir(product_images):
    print("object: ",obj)

'''
Xoá phong nên ở phía sau và tự động sao lưu bản hoàn thiện
vào thư mục kết quả được chỉ định
'''

def removing_background(filename:str):
    try:
        session = new_session("u2net")
        output_path = os.path.join(ROOT,'data','bg_images')
        input_path = os.listdir(filename)
        
        for obj in input_path:
            data = os.path.join(filename,obj)
            
            if not os.path.isfile(data):
                continue
            
            if not obj.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
                continue
            
            pure_image = Image.open(data)
            output_res = remove(pure_image, session=session)
            output_name = os.path.splitext(obj)[0]
            output_data = os.path.join(output_path,f'{output_name}.png')
            output_res.save(output_data)
            print(f'image {obj} has been proccessed !!!')
    except Exception as error:
        return {
            "error":str(error)
        }



if __name__ == "__main__":
    print(removing_background(product_images))