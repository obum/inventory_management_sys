from product_store import Product_store
from product import Product

def main():
    print('Welcome to ShopRite Stores Inventory System\nEnter the following commands to utlize the system\n\n')
    product = Product()
    shop_rite = Product_store()
    while True:
        user_command = input(f'Enter "c" to create a product,\nEnter "a" to add the product,\nEnter "v" to view all products\nEnter "u" to update a products details,\nEnter "r" to restock a products quantity\nEnter "x" to exit the system\nEnter command here >>>> ')
        print()
        match user_command:
            case "c":
                product.create_product()
                print()
            case "a":
                shop_rite.add_new_product(product)
                print()
            case "v":
                print(shop_rite.view_all_product())
                print()
            case "u":
                shop_rite.update_product_detail()
                print()
            case "r":
                shop_rite.restock_product_quantity()
                print()
            case "x":
                print('Goodbye from ShopRite Inventory System')
                break
        
        

if __name__ == '__main__':
    main()