from dataclasses import dataclass

@dataclass()
class Product:
    sku: str
    desc: str
    photo: str
    available_qty: int
    price: float
    
