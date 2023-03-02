from ..domain.product import Product
from ..domain.exceptions import InvalidProductException, ProductDoesNotExistExcpetion

class Warehouse:
    def __init__(self, repository):
        self.repository = repository
        
    def add_new_product(self, product: Product):
        if product.available_qty >= 0:
            self.repository.add(product)
        else:    
            raise InvalidProductException("Product is invalid because negative quantity")
        
    def get_product(self, product_id):
        product = self.repository.get(product_id)
        if not product:
            raise ProductDoesNotExistExcpetion("Product does not exist")
        return product

    def delete_product(self, product_id):
        product = self.get_product(product_id)
        self.repository.delete(product)
        
    def get_all_products(self):
        return self.repository.list()
        
        
                
                
            
                
            
        
        
        
    