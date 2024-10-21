# from mysql.connector.cursor import MySQLCursor
# from sqlite3 import connect
# from traceback import print_list
# from unittest import result
import Mysqlsever
from product import Product


connection = Mysqlsever.create_connection()

cursor = connection.cursor()


class Product_store:
    def __init__(self) -> None:
        self.shelf: list[Product] = []
        
    def add_new_product(self, a_product: Product):

        # self.shelf.append(a_product)
        # print(f"{a_product.product_name} Added")
        
        add_new_product_query = f"""
            INSERT INTO products
            (product_name, category, stock_quantity, price)
            VALUES
            (%s, %s, %s, %s);
            """
        cursor.execute(add_new_product_query, (a_product.product_name, a_product.product_category, a_product.quantity, a_product.product_price))
        connection.commit()
        print()
        print(f'product: {a_product.__str__()} added successfully')
        
    # def get_column_names(self):
    #     get_column_names_query = """
    #         SELECT COLUMN_NAME
    #         FROM INFORMATION_SCHEMA.COLUMNS
    #         WHERE TABLE_NAME = 'your_table_name';
    #     """
    
        
        
    def view_all_product(self):
        
        view_all_product_query = """
            SELECT * 
            FROM products
        """
        
        cursor.execute(view_all_product_query)
        
        all_products = cursor.fetchall()
        
        id_list = [product[0] for product in all_products]
        
        products = {key: value for key, value in zip(id_list, all_products)}
        
        return (products)
    
    def update_product_detail(self):
        
        product_list = self.view_all_product()
        id = list(product_list.keys())
        product_to_change = int(input(f'Choose from {id} the product_id you wish to change: '))
        print()
        product__details_to_change = product_list[product_to_change]
        print(f'You want to change product {product_to_change}')
        for detail,w in zip(product__details_to_change, ('product_id','product_name', 'category', 'stock_quantity', 'price')):
            print(f'{w} : {detail}')
        print()    
        new_name = str(input(f'Enter the new product name: '))
        new_category = str(input(f'Enter the new product category: '))
        new_price = float(input(f'Enter the new product price: '))
        
        update_detail_query = f"""
            UPDATE products
            SET product_name = %s, category = %s, price = %s
            WHERE product_id = %s; 
        """
        
        cursor.execute(update_detail_query, (new_name, new_category, new_price, product_to_change))
        connection.commit()
        
        new_list = self.view_all_product()
        print()
        print(f'Product Details Change Succsessful')
        for old,detail,w in zip(product__details_to_change, ('product_id','product_name', 'category', 'stock_quantity', 'price'), new_list[product_to_change]):
            if detail == 'product_id' or detail == 'stock_quantity':
                continue
            print(f'You have changed {detail}: from {old} to {w}')

    def restock_product_quantity(self):
        
        product_list = self.view_all_product()
        id = list(product_list.keys())
        product_to_change = int(input(f'Choose from {id} the product_id you wish to restock: '))
        print()
        product__details_to_change = product_list[product_to_change]
        print(f'You want to restock product {product_to_change}')
        for detail,w in zip(product__details_to_change, ('product_id','product_name', 'category', 'stock_quantity', 'price')):
            if  w == 'stock_quantity' or w == 'product_name':
                print(f'{w} : {detail}')
            
        print()    
        new_quantity = float(input(f'Enter the new product quantity: '))
        
        update_detail_query = f"""
            UPDATE products
            SET stock_quantity = %s
            WHERE product_id = %s; 
        """
        
        cursor.execute(update_detail_query, (new_quantity, product_to_change))
        connection.commit()
        
        new_list = self.view_all_product()
        print()
        print(f'Product Restock Succsessful')
        for old,detail,w in zip(product__details_to_change, ('product_id','product_name', 'category', 'stock_quantity', 'price'), new_list[product_to_change]):
            if  detail != 'stock_quantity':
                continue
            print(f'You have changed {detail}: from {old} to {w}')
