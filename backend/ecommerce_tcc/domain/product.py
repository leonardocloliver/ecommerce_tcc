from dataclasses import dataclass

@dataclass()
class Product:
    uuid: str
    sku: str
    desc: str
    photo: str
    available_qty: int
    price: float
    
