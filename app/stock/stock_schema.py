from pydantic import BaseModel

class ProductStockListResponse(BaseModel):
    container_name: str
    quantity: int

class ProductStockResponse(BaseModel):
    total_stock: int
    stock_data: list[ProductStockListResponse]

class TotalProductStockResponse(BaseModel):
    product_code: str
    total_stock: int
    stock_data: list[ProductStockListResponse]

class ContainerStockListResponse(BaseModel):
    product_code: str
    quantity: int

class ContainerStockResponse(BaseModel):
    stock_data: list[ContainerStockListResponse]

class TotalContainerStockResponse(BaseModel):
    container_name: str
    total_stock: int
    stock_data: list[ContainerStockListResponse]
