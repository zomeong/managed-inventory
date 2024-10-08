from fastapi import APIRouter, Depends
from app.product.product_service import ProductService
from app.product.product_schema import ProductCreate, ProductUpdate, ProductResponse
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.exception_handler import exception_handler

router = APIRouter(
    prefix="/products",
)

def get_product_service(db: Session = Depends(get_db)):
    return ProductService(db)

@router.post("")
@exception_handler
def create_product(product: ProductCreate, service: ProductService = Depends(get_product_service)):
    service.create_product(product)
    return "물품 생성이 완료되었습니다."

@router.get("/{product_id}", response_model=ProductResponse)
@exception_handler
def get_product(product_id:int, service: ProductService = Depends(get_product_service)):
    return service.get_product(product_id)

@router.get("", response_model=list[ProductResponse])
@exception_handler
def get_all_products(service: ProductService = Depends(get_product_service)):
    return service.get_all_products()
    
@router.get("/search/name/{product_name}", response_model=list[ProductResponse])
@exception_handler
def search_products_by_name(product_name: str, service: ProductService = Depends(get_product_service)):
    return service.search_products_by_name(product_name)

@router.get("/search/code/{product_code}", response_model=list[ProductResponse])
@exception_handler
def search_products_by_code(product_code: str, service: ProductService = Depends(get_product_service)):
    return service.search_products_by_code(product_code)

@router.post("/{product_id}/update")
@exception_handler
def update_product(product_id: int, product: ProductUpdate,
                service: ProductService = Depends(get_product_service)):
    service.update_product(product_id, product)
    return "물품 정보 수정이 완료되었습니다."
