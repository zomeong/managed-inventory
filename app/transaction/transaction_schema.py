from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum

class TransactionType(str, Enum):
    IN = "입고"
    OUT = "출고"

class TransactionBase(BaseModel):
    id: int = Field(alias="_id")
    type: TransactionType
    product_code: str
    container_name: str
    quantity: int = Field(ge=1, description="1개 이상 입/출고 가능합니다.")
    date: datetime

class TransactionCreate(TransactionBase):
    pass

class TransactionResponse(TransactionBase):
    pass