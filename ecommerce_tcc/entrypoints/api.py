import fastapi as _fastapi
from fastapi import Request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ecommerce_tcc.adapters import orm
from ecommerce_tcc.adapters.product_repository import ProductRepository
from ecommerce_tcc.services.warehouse import Warehouse
from ecommerce_tcc.domain.product import Product
from .config import get_postgres_uri


orm.start_mappers()
get_session = sessionmaker(bind=create_engine(get_postgres_uri()))
app = _fastapi.FastAPI()


# TODO: SUBSTITUIR REQUEST GENERICO COM PYDANTIC
@app.post("/v1/api/products/")
async def create_product(request : Request):
    session = get_session()
    repo = ProductRepository(session)
    warehouse = Warehouse(repo)
    response = await request.json()
    product = Product(sku=response["sku"], desc=response["desc"], photo=response["photo"], available_qty=response["available_qty"], price=response["price"])
    warehouse.add_new_product(product)
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