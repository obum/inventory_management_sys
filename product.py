class Product:
    def __init__(self):
        self.product_name = ''
        self.product_category = ''
        self.quantity = 0
        self.product_price = 0
        self.inventory_list: list[dict] = []
        
    def __str__(self) -> str:
        return f"Product: {self.product_name}, \nCategory: {self.product_category}, \nstock_quantity: {self.quantity}, \nprice: {self.product_price}"
    
    def create_product(self):
        self.product_name : str = input(f'Enter the product name : ')
        self.product_category :str = input(f'Enter the product category : ')
        self.quantity: int = input(f'Enter the product quanity : ')
        self.product_price : float = input(f'Enter the product price : ')
        return self

