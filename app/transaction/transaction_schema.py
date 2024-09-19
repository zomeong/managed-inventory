from pydantic import BaseModel
from datetime import datetime

class TransactionResponse(BaseModel):
    _type: str
    product_code: str
    container_name: str
    quantity: int
    date: datetime
    manager_name: str