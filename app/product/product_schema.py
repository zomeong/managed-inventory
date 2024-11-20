from pydantic import BaseModel, Field
from typing import Optional

class ProductBase(BaseModel):
    name: str
    code: str

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    name: Optional[str] = None
    code: Optional[str] = None

class ProductResponse(ProductBase):
    _id: int