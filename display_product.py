from main import Product


products = Product.select()
for product in products:
    print(product.product_color, product.product_quantity, product.product_description, product.product_color)