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
        
    def get_product(self, _id):
        product = self.repository.get(_id)
        if not product:
            raise ProductDoesNotExistExcpetion("Product does not exist")
    
    # TODO : ATUALIZAR COM O PRODUCT REPOSITORY
    # def update_product(self, updated_product: Product):
    #     found = False
    #     for index, product in enumerate(self.stock):
    #         if product._id == updated_product._id:
    #            self.stock[index] = updated_product
    #            found = True
    #     if not found:
    #         raise ProductDoesNotExistExcpetion("Product does not exist")

    
    # TODO : DELETAR COM PRODUCT REPOSITORY
    # def delete_product(self, delete_product):
    #     self.stock.remove(delete_product)
        
    def get_all_products(self):
        return self.repository.list()
        
        
                
                
            
                
            
        
        
        
    