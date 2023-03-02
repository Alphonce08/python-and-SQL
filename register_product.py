from main import Product

try:
    product_price = input("Enter price \n")
    product_quantity = input("Enter quantity \n")
    product_description = input("Enter description \n")
    product_color = input("Enter color \n")

    Product.create(product_price=product_price, product_quantity=product_quantity, product_description=product_description, product_color=product_color)
    print("your product is successfully order")
except:
    print("fail to provide real identity of product")