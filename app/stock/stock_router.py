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

@router.get("/products/{product_code}", response_model=ProductStockResponse,
    description="""
    특정 물품 재고 조회 API

    Parameter
    - product_code: 물품 코드

    Output
    - total_stock: 전체 재고
    - stock_data: 창고별 재고
        [
        - container_name: 창고 이름
        - quantity: 해당 창고에 저장된 재고
        ]
    """)
@exception_handler
def get_product_stock(product_code: str, service: StockService = Depends(get_stock_service)):
    stock_data, total_stock = service.get_product_stock(product_code)

    return ProductStockResponse(
        total_stock=total_stock,
        stock_data=[
            ProductStockListResponse(container_name=item[0], quantity=item[1])
            for item in stock_data
        ]
    )

@router.get("/containers/{container_name}", response_model=list[ContainerStockListResponse],
    description="""
    특정 창고 재고 조회 API

    Parameter
    - container_name: 창고 이름

    Output
    [
    - product_code: 물품 코드
    - quantity: 해당 물품 재고
    ]
    """)
@exception_handler
def get_container_stock(container_name: str, service: StockService = Depends(get_stock_service)):
    stock_data = service.get_container_stock(container_name)

    return [
            ContainerStockListResponse(product_code=item[0], quantity=item[1])
            for item in stock_data
        ]

@router.get("/products", response_model=list[TotalProductStockResponse],
    description="""
    전체 물품 재고 조회 API

    Output
    - product_code: 물품 코드
    - total_stock: 물품의 전체 재고
    - stock_data: 물품의 창고별 재고
        [
        - container_name 창고 이름
        - quantity: 창고에 저장된 재고
        ]
    """)
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

@router.get("/containers", response_model=list[TotalContainerStockResponse],
    description="""
    전체 창고 재고 조회 API

    Output
    - container_name: 창고 이름
    - total_stock: 창고의 전체 재고
    - stock_data: 창고의 물품별 재고
        [
        - product_code: 물품 코드
        - quantity : 해당 물품 재고
        ]
    """)
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
