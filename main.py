from product_store import Product_store
from product import Product

def main():
    # product = Product().get_product()
    shop_rite = Product_store()
    # shop_rite.add_new_product(product)
    shop_rite.view_all_product()

if __name__ == '__main__':
    main()