from pydantic import BaseModel 

class Product(BaseModel):
    sku: str
    desc: str
    photo: str
    available_qty: int
    price: str

    class Config:
        orm_model = True