class Product:
    def __init__(self):
        self.product_name = ''
        self.product_category = ''
        self.quantity = 0
        self.product_price = 0
        self.inventory_list: list[dict] = []
        
    def __str__(self) -> str:
        return f"{self.product_name}, \nCategory: {self.product_category}, \nstock_quantity: {self.quantity}, \nprice: {self.product_price}"
    
    def create_product(self):
        self.product_name : str = input(f'Enter the product name : ')
        self.product_category :str = input(f'Enter the product category : ')
        self.quantity: int = input(f'Enter the product quanity : ')
        self.product_price : float = input(f'Enter the product price : ')
        return self
        
    
   
    # def add_new_product(self, cursor: MySQLCursor):
    #     """Store the product name, category (e.g., electronics, groceries), stock quantity, and price."""
    #     product = {
    #         'name':  self.product_name,
    #         'category': self.product_category,
    #         'quantity': self.quantity,
    #         'price': self.product_price
    #     }
    #     self.inventory_store.append(product)
    #     cursor.execute()
    #     print(self.inventory_store)
    
    # def view_all_product(self):
    #     pass
    
    # def update_product_details(self):
    #     pass
    
    # def remove_a_product(self):
    #     pass
    
    # def low_stock_alert(self):
    #     pass
    
    # def search_product(self):
    #     pass
    
    # def sort_product(self):
    #     pass
  
  
# phone = Product('phone', 'electronic', 1, 15000)  
# print(phone)
