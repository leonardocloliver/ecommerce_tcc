from .product import Product

class Warehouse:
    def __init__(self):
        self.stock = []
        
    def add_new_product(self, product: Product):
        self.stock.append(product)
        
    def get_product(self, _id):
        for product in self.stock:
            if product._id == _id:
                return product
        return None
    
    def update_product(self, updated_product: Product):
        for index, product in enumerate(self.stock):
            if product._id == updated_product._id:
                self.stock[index] = updated_product
    
    def delete_product(self, delete_product):
        self.stock.remove(delete_product)
        
    def get_all_products(self):
        return self.stock
        
        
                
                
            
                
            
        
        
        
    