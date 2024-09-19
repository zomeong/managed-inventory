from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class TransactionType(str, Enum):
    IN = "입고"
    OUT = "출고"

class TransactionBase(BaseModel):
    type: TransactionType
    product_code: str
    container_name: str
    quantity: int

class TransactionCreate(TransactionBase):
    pass

class TransactionResponse(TransactionBase):
    _id: int
    date: datetime