from pydantic import BaseModel
# from typing import List

class ProductCreateUpdate(BaseModel):
    sku: str
    desc: str
    photo: str
    available_qty: int
    price: str

    class Config:
        orm_model = True

class Product(BaseModel):
    uuid: str
    sku: str
    desc: str
    photo: str
    available_qty: int
    price: str

    class Config:
        orm_model = True
    
    

# class PaginatedProduct(BaseModel):
#     # limit: int
#     # offset: int 
#     data: List[Product]