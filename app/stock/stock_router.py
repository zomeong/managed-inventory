from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.stock.stock_service import StockService
from app.stock.stock_schema import ProductStockResponse, ProductStockListResponse, ContainerStockListResponse, TotalProductStockResponse, TotalContainerStockResponse
from app.core.exception_handler import exception_handler


router = APIRouter(
    prefix="/stock",
)

def get_stock_service(db:Session = Depends(get_db)):
    return StockService(db)

@router.get("/products/{product_id}", response_model=ProductStockResponse)
@exception_handler
def get_product_stock(product_id: int, service: StockService = Depends(get_stock_service)):
    stock_data, total_stock = service.get_product_stock(product_id)

    return ProductStockResponse(
        total_stock=total_stock,
        stock_data=[
            ProductStockListResponse(container_name=item[0], quantity=item[1])
            for item in stock_data
        ]
    )

@router.get("/containers/{container_id}", response_model=list[ContainerStockListResponse])
@exception_handler
def get_container_stock(container_id: int, service: StockService = Depends(get_stock_service)):
    stock_data = service.get_container_stock(container_id)

    return [
            ContainerStockListResponse(product_code=item[0], quantity=item[1])
            for item in stock_data
        ]

@router.get("/products", response_model=list[TotalProductStockResponse])
@exception_handler
def get_all_products_stock(service: StockService = Depends(get_stock_service)):
    stock_map = service.get_all_products_stock()

    return [
        TotalProductStockResponse(
            product_code=product_code,
            total_stock=stock["total_stock"],
            stock_data=[
                ProductStockListResponse(container_name=item["container_name"], quantity=item["quantity"])
                for item in stock["stock_data"]
            ]
        )
        for product_code, stock in stock_map.items()
    ]

@router.get("/containers", response_model=list[TotalContainerStockResponse])
@exception_handler
def get_all_containers_stock(service: StockService = Depends(get_stock_service)):
    stock_map = service.get_all_containers_stock()

    return [
        TotalContainerStockResponse(
            container_name=container_name,
            total_stock=stock["total_stock"],
            stock_data=[
                ContainerStockListResponse(product_code=item["product_code"], quantity=item["quantity"])
                for item in stock["stock_data"]
            ]
        )
        for container_name, stock in stock_map.items()
    ]
