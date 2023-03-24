import fastapi as _fastapi
from fastapi import Request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ecommerce_tcc.adapters.product_repository import ProductRepository
from ecommerce_tcc.services.warehouse import Warehouse
from .config import get_postgres_uri
from .schema import Product, ProductCreateUpdate

get_session = sessionmaker(bind=create_engine(get_postgres_uri()))
app = _fastapi.FastAPI()


@app.post("/v1/api/products/")
async def create_product(product: ProductCreateUpdate):
    session = get_session()
    repo = ProductRepository(session)
    warehouse = Warehouse(repo)
    warehouse.add_new_product(product.dict())
    return "OK", 201

@app.delete("/v1/api/products/{product_id}")
async def delete_product(product_id):
    session = get_session()
    repo = ProductRepository(session)
    warehouse = Warehouse(repo)
    warehouse.delete_product(product_id)
    return "OK", 200

@app.get("/v1/api/products/{product_id}")
async def get_product(product_id):
    session = get_session()
    repo = ProductRepository(session)
    warehouse = Warehouse(repo)
    product = warehouse.get_product(product_id)
    return product

@app.get("/v1/api/products/")
async def get_all_products():
    session = get_session()
    repo = ProductRepository(session)
    warehouse = Warehouse(repo)
    products = warehouse.get_all_products()
    return products

@app.put("/v1/api/products/{product_id}")
async def update_product(product_id, product_to_update: ProductCreateUpdate):
    session = get_session()
    repo = ProductRepository(session)
    warehouse = Warehouse(repo)
    updated_product = warehouse.update_product(product_id, product_to_update.dict())
    return updated_product
