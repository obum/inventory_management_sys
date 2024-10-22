# Introductory Notes

Welcome to the *'Easy project - Inventory management System'* 

This project is a Python sccript that interacts with a MySQL database using the `mysql.connector` library. 

In this project, there are four Python files:
- `main.py`: This is the main entry point into the inventory system, it handles the core system logic, control flow and user interface on the terminal.
- `Mysqlsever.py`: A module that handles the setup and creation of the MySQL connection.
- `Product_store.py`: A module that handles all SQL CRUD operations and the inventory system feature and functionalities.
- `Product.py`: A module that creates the product class and tries to handle its attributes and functionality.


---------------------------------------------------------------------------------

# README for MySQL Connection Script - Mysqlsever.py

This script creates a connection to a MySQL database *'product_store'* using the `mysql.connector` library and includes basic error handling.

### Key Components:

1. **Create Connection function**:  
   The `create_connection` function contains:
   - `connection`: A variable that holds the `connect()` method from the mysql-connector library.
   - `user`: Your MySQL username.
   - `host`: The MySQL server (default is `localhost`).
   - `password`: Your MySQL password.
   - `database_name`: Name of the database (`product_store`).

2. **Error Handling**:  
   Simple error handling for:
   - Confirmation of connection.
   - decalartion of the cursor and connection object.
   - Database not found.
   And general handling for other errors.


---

# README for Product

The `product.py` file is a module to help create and handle the product object creation and its attributes.


### Key Features:

- **Product object constructor**:  
  Defines the attributes frequired for a product in the inventory management system.

- **Product string**:  
  Defines the string representation for the product.

- **Methods in `product.py`**:
  - `create_product()`: creates a product object.

---

# README for Product_store

This project is an Inventory Management System built with Python and MySQL. 
You can manage products in a database, including adding, updating, deleting, and viewing products, plus a handy stock alert for low inventory.

### Key Features:

- **Database Connection**:  
  imports the `connection` and `cursor` objects from the Mysqlsever.py module.

- **Product_store Class**:  
  Contains methods for all database operations like creating a database, adding products, updating quantities, and more.

- **Methods in `product_store.py`**:
  - `add_new_product()`: Adds products.
  - `all_product_table()`: Displays the current inventory balance to the terminal in a clean table format.
  - `view_all_product()`: A method that returns all product object as dictionary.
  - `update_product_detail()`: Updates the product details.
  - `restock_product_quantity()`: Updates stock quantity.
  - `delete_a_product()`: Removes products by ID.
  - `search_name_and_category()`: Search the database for a product by name or category.
  - `sort_products()`: Sorts products (by price or quantity).
  - `check_low_stock_alert()`: Alerts you for low stock.

- **Closing the Connection**:  
  The `close()` method ensures the cursor and connection are properly closed after operations.

---

# README for main.py

`main.py` is the entry point of the Inventory Management System, it handles the core program logic and controls the inventory system's Command Line Interface interaction with the user.

### Main Features:

- **Menu Options**:  
  Displays a menu with options like creating a product, adding the created product to inventory, updating stock details, deleting a product, and more.

- **Core Operations**:  
  Based on the user’s menu selection, the program calls the appropriate methods from `product_store` to handle tasks like, this is done using match-case control flow:
  - Creating a product.
  - Adding and updating products.
  - Viewing and sorting inventory.
  - Stock alerts for low quantities.
  - Exiting the inventory management system.


This file is designed to make managing your inventory easy through simple command-line inputs.

<!-- # BUGS IN CURRENT IMPLEMENTATION
  To be updated... -->

# CHALLENGES FACED SO FAR

- There are issues with explicitly importing the `connection` and `cursor` object from the Mysqlsever module; currently I have to import the module and reference the object from methods to get the program to work.
