from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String

class Base(DeclarativeBase):
    pass


class Product(Base):
    __tablename__ = 'product'
    
    uuid: Mapped[str] = mapped_column(primary_key=True)
    sku: Mapped[str] 
    desc: Mapped[str] = mapped_column(String(255))
    photo: Mapped[str] 
    available_qty: Mapped[int]
    price: Mapped[str] 










 

