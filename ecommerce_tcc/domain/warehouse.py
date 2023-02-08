from .product import Product
from .exceptions import InvalidProductException, ProductDoesNotExistExcpetion

class Warehouse:
    def __init__(self):
        self.stock = []
        
    def add_new_product(self, product: Product):
        if product.available_qty >= 0:
            self.stock.append(product)
        else:    
            raise InvalidProductException("Product is invalid because negative quantity")
        
    def get_product(self, _id):
        for product in self.stock:
            if product._id == _id:
                return product
        raise ProductDoesNotExistExcpetion("Product does not exist")
    
    def update_product(self, updated_product: Product):
        found = False
        for index, product in enumerate(self.stock):
            if product._id == updated_product._id:
               self.stock[index] = updated_product
               found = True
        if not found:
            raise ProductDoesNotExistExcpetion("Product does not exist")

    
    def delete_product(self, delete_product):
        self.stock.remove(delete_product)
        
    def get_all_products(self):
        return self.stock
        
        
                
                
            
                
            
        
        
        
    