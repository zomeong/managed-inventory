from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.stock.stock_service import StockService
from app.stock.stock_schema import ProductStockResponse, ContainerStockResponse

router = APIRouter()

def get_stock_service(db:Session = Depends(get_db)):
    return StockService(db)

@router.get("/products/stock/{product_id}", response_model=ProductStockResponse)
def get_product_stock(product_id: int, service: StockService = Depends(get_stock_service)):
    stock_data, total_stock = service.get_product_stock(product_id)

    return {
        "total_stock" : total_stock,
        "stock_data" : stock_data
    }

@router.get("/containers/stock/{container_id}", response_model=ContainerStockResponse)
def get_container_stock(container_id: int, service: StockService = Depends(get_stock_service)):
    stock_data = service.get_container_stock(container_id)

    return {
        "stock_data" : stock_data
    }
