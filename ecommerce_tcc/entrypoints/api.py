import fastapi as _fastapi
from fastapi import Request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ecommerce_tcc.adapters import orm
from ecommerce_tcc.adapters.product_repository import ProductRepository
from pydantic import BaseModel
from ecommerce_tcc.services.warehouse import Warehouse


# TODO : IMPLEMENTAR CONFIGURACAO
def get_postgres_uri():
    host = "db"
    port = 5432 
    password = "admin"
    user, db_name = "admin", "ecommerce"
    return f"postgresql://{user}:{password}@{host}:{port}/{db_name}"

orm.start_mappers()
get_session = sessionmaker(bind=create_engine(get_postgres_uri()))
app = _fastapi.FastAPI()


from ecommerce_tcc.domain.product import Product
    
# TODO: SUBSTITUIR REQUEST GENERICO COM PYDANTIC
@app.post("/v1/api/products/")
async def create_product(request : Request):
    session = get_session()
    repo = ProductRepository(session)
    warehouse = Warehouse(repo)
    response = await request.json()
    product = Product(name=response["name"], desc=response["desc"], photo=response["photo"], available_qty=response["available_qty"], price=response["price"])
    warehouse.add_new_product(product)
    return "OK", 201