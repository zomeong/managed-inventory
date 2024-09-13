from pydantic import BaseModel

class StockBase(BaseModel):
    product_id: int
    warehouse_id: int
    quantity: float

class Stock(StockBase):
    _id: int