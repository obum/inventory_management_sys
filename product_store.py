# from mysql.connector.cursor import MySQLCursor
# from sqlite3 import connect
# from traceback import print_list
# from unittest import result
# from numpy import delete
import Mysqlsever
from product import Product
from prettytable import PrettyTable


connection = Mysqlsever.create_connection()

cursor = connection.cursor()




safety_stock = 5

class Product_store:
    def __init__(self) -> None:
        self.shelf: list[Product] = []
        
    def add_new_product(self, a_product: Product):

        add_new_product_query = f"""
            INSERT INTO products
            (product_name, category, stock_quantity, price)
            VALUES
            (%s, %s, %s, %s);
            """
        self.outcome = ''
        for product in list(self.view_all_product().values()):
            if a_product.product_name == product[1]:
                self.outcome = 'a'
            elif a_product.product_name == "":
                self.outcome = 'b'
            else:
                self.outcome = 'c'
        if self.outcome == 'c':
                cursor.execute(add_new_product_query, (a_product.product_name, a_product.product_category, a_product.quantity, a_product.product_price))
                connection.commit()
                print()
                print(f'product added successfully:\n{a_product.__str__()}')
        if self.outcome == 'b':
            print('No product found: Create product, before adding to inventory')
            
        if self.outcome == 'a':
            print(f'product already exists:\n{a_product.__str__()}')
        
    def all_product_table(self):
        self.table = PrettyTable()
        view_all_product_query = """
            SELECT * 
            FROM products
        """
        
        cursor.execute(view_all_product_query)
        
        all_products = cursor.fetchall()
        
        id_list = [product[0] for product in all_products]
        
        products = {key: value for key, value in zip(id_list, all_products)}
        
        self.table.field_names = ["Product_id", "Product_name", "Category", "Stock Quantity", "Price"]
        for line in list(products.values()):
            self.table.add_row(line)
        self.table.align = "l"
        print(self.table)
      
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

    def delete_a_product(self):
        product_list = self.view_all_product()
        id = list(product_list.keys())
        product_to_delete = int(input(f'Enter a product_id {id} to delete: '))
        print()
        product_details_to_delete = product_list[product_to_delete]
        print(f'You want to delete product {product_to_delete}')
        for detail,w in zip(product_details_to_delete, ('product_id','product_name', 'category', 'stock_quantity', 'price')):
            print(f'{w} : {detail}')
        print()
        
        delete_product_query = f"""
            DELETE FROM products
            WHERE product_id = %s; 
        """
        cursor.execute(delete_product_query, (product_to_delete,))
        connection.commit()
        print()
        print(f'{product_details_to_delete[1] } Deleted Succsessfully')
        
    
    def check_low_stock_alert(self):
        
        print(f'List of products with stock below saftety stock level (5)')
        product_list = self.view_all_product().values()
        
        self.low_stock_products = []
        self.product_ids = []
        self.check_ss_table = PrettyTable()
        
        for product in product_list:
            if product[3] < safety_stock:
                if product[0] not in self.product_ids:
                    self.product_ids.append(product[0])
                    self.low_stock_products.append(product)
                
        self.check_ss_table.field_names = ["Product_id", "Product_name", "Category", "Stock Quantity", "Price"]
        for line in self.low_stock_products:
            self.check_ss_table.add_row(line)
        self.check_ss_table.align = "l"
        print(self.check_ss_table)
        
    def search_name_and_category(self):
        self.user_input = input('Search for a product name or category: ').lower()
        
        product_list = list(self.view_all_product().values())
        # print(product_list, product_list[1])
        
        self.name_list = [product[1] for product in product_list]
        self.category_list = [product[2] for product in product_list]
        self.found_items = []
        self.search_table = PrettyTable()
        
        for prodcut, name, category in zip(product_list, self.name_list, self.category_list):
            if self.user_input == name.lower() or self.user_input == category.lower():
                self.found_items.append(prodcut)
        
        if len(self.found_items) == 0:
            print(f'"{self.user_input}" not found in database')
            
        else:        
            self.search_table.field_names = ["Product_id", "Product_name", "Category", "Stock Quantity", "Price"]
            for line in self.found_items:
                self.search_table.add_row(line)
            self.search_table.align = "l"
            print(self.search_table)
                    
                
                
        