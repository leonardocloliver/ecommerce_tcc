from sqlalchemy.orm import mapper
from sqlalchemy import MetaData, Table, Column, Integer, String
from ecommerce_tcc.domain.product import Product

metadata = MetaData()


product = Table(
    'product', metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("sku", String(255)),
    Column("desc", String(255)),
    Column("photo", String(255)),
    Column("available_qty", Integer),
    Column("price", String(255))
)

def start_mappers():
    product_mapper = mapper(Product, product)









 

