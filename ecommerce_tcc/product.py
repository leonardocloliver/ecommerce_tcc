from dataclasses import dataclass

@dataclass(frozen=True)
class Product:
    _id: str
    name: str
    desc: str
    photo: str
    available_qty: int
    price: float
    
