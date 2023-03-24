from .models import Product

class ProductRepository:
    def __init__(self, session):
        self.session = session
    
    def add(self, product: Product):
        self.session.add(product)
        self.session.commit()
    
    def get(self, product_id):
        return self.session.query(Product).get(product_id)
    
    def list(self):
        return self.session.query(Product).all()
    
    def delete(self, product: Product):
        self.session.delete(product)
        self.session.commit()
        
    def update(self, product: Product):
        product_details = self.get(product.uuid)
        product_details.available_qty = product.available_qty
        product_details.sku = product.sku
        product_details.desc = product.desc
        product_details.photo = product.photo
        product_details.price = product.price
        self.session.commit()
        return product_details