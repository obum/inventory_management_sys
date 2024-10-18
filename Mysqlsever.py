from mysql.connector import connect, Error
from product import Product

DB_NAME = 'product_store'

# Add a product to database table

add_new_product_query = f"""
INSERT INTO products
(product_name, category, stock_quantity, price)
VALUES
();
"""
def sql_cursor():
    try:
        with connect(host= 'localhost', user= 'root', password= 'Stevengerad8!', database= f'{DB_NAME}') as connection:
            with connection.cursor() as cursor:
                return cursor
        
    except Error as err:
        print(err.msg)
        
    finally:
        return cursor