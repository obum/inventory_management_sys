from mysql.connector import connect

DB_NAME = 'product_store'

# A function to return a database connection

def create_connection():
    connection = connect(
        host= "localhost",
        user= "root",
        password= "Stevengerad8!",
        database= DB_NAME )
    return connection