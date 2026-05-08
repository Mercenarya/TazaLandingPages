# config.py
url = "https://hderma.vn/cua-hang/"
products_store_xpath = "//div[contains(@class, 'product-grid-item')]"

# Lưu ý: Thêm dấu "." ở đầu để chỉ định đây là XPath tương đối
product_name = ".//h3[@class='wd-entities-title']/a"
product_details = ".//span[@class='price']" # Thường giá sẽ nằm ở đây
product_images = ".//img[contains(@class, 'attachment')]"