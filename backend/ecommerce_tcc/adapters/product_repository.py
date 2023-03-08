from ecommerce_tcc.domain.product import Product

class ProductRepository:
    def __init__(self, session):
        self.session = session
    
    def add(self, product: Product):
        self.session.add(product)
        self.session.commit()
    
    def get(self, product_id):
        return self.session.query(Product).filter_by(uuid=product_id).one()
    
    def list(self):
        return self.session.query(Product).all()
    
    def delete(self, product: Product):
        self.session.delete(product)
        self.session.commit()
        