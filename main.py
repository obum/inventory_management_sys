from product_store import Product_store
from product import Product

def main():
    print('Welcome to ShopRite Stores Inventory System\nEnter the following commands to utlize the system\n\n')
    product = Product()
    shop_rite = Product_store()
    while True:
        user_command = input(f'Enter "c" to create a product.\nEnter "a" to add the product to inventory.\nEnter "v" to view all products.\nEnter "u" to update a products details.\nEnter "r" to restock a products quantity.\nEnter "d" to delete a product.\nEnter "s" to display products with low quantities.\nEnter "search" to Search products by name or category.\nEnter "sort" to Sort products by price or stock quantity.\nEnter "x" to exit the system.\nEnter command here >>>> ').lower()
        print()
        match user_command:
            case "c":
                product.create_product()
                print()
            case "a":
                shop_rite.add_new_product(product)
                print()
            case "v":
                shop_rite.all_product_table()
                print()
            case "u":
                shop_rite.update_product_detail()
                print()
            case "r":
                shop_rite.restock_product_quantity()
                print()
            case "d":
                shop_rite.delete_a_product()
                print()    
            case "s":
                shop_rite.check_low_stock_alert()
                print()           
            case "search":
                shop_rite.search_name_and_category()
                print()
            case "sort":
                shop_rite.sort_products()
                print()
            case "x":
                print('Goodbye from ShopRite Inventory System.')
                break
            case _:
                print('Unknow command: Try agin!!!')
                print()
        
        

if __name__ == '__main__':
    main()