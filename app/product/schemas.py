from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    code: str
    
class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class Product(ProductBase):
    _id: int