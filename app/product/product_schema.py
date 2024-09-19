from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    name: str
    code: str

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    code: Optional[str] = None