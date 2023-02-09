from dataclasses import dataclass

@dataclass()
class Product:
    name: str
    desc: str
    photo: str
    available_qty: int
    price: float
    
