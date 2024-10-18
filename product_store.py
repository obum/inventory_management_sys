# from mysql.connector.cursor import MySQLCursor
# from sqlite3 import connect
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
        
        print(f'product: {a_product.__str__()} added successfully')
    
        
        
    # def view_all_product(self):
    #     for item in self.shelf:
    #         print(item.product_name, item.quantity)
        
