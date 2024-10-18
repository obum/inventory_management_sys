class Product:
    def __init__(self, name: str, category: str, price: float = 0, quantity: int =0):
        self.product_name = name
        self.product_category = category
        self.quantity = quantity
        self.product_price = price
        self.inventory_list: list[dict] = []
        
    def __str__(self) -> str:
        return f"Product: {self.product_name}, Category: {self.product_category}, stock_quantity: {self.quantity}, price: {self.product_price}"
        
    
   
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
  
  
phone = Product('phone', 'electronic', 1, 15000)  

def main():   
    print(phone)
    
if __name__ == "__main__":
    main()