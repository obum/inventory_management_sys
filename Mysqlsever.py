from mysql.connector import connect, Error

DB_NAME = 'product_store'

# A function to return a database connection

def create_connection():
    
    a_connection = connect(
        host= "localhost",
        user= "root",
        password= "Stevengerad8!",
        database= DB_NAME )
    return a_connection

try:
    connection = create_connection()
    
    if connection and connection.is_connected():
        mycursor = create_connection().cursor()
        print(f'Database Conncetion Succesful: {connection.get_server_info()}')
        print()
    
except Error as err:
    print(f'Connection Error: {err.msg}')
    

