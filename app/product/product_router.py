from fastapi import APIRouter, Depends
from app.product.product_service import ProductService
from app.product.product_schema import ProductCreate, ProductUpdate, ProductResponse
from sqlalchemy.orm import Session
from app.core.database import get_db

router = APIRouter(
    prefix="/products",
)

def get_product_service(db: Session = Depends(get_db)):
    return ProductService(db)

@router.post("")
def create_product(product: ProductCreate, service: ProductService = Depends(get_product_service)):
    service.create_product(product)
    return "물품 생성이 완료되었습니다."

@router.get("/{product_id}", response_model=ProductResponse)
def get_product(product_id:int, service: ProductService = Depends(get_product_service)):
    return service.get_product(product_id)

@router.get("", response_model=list[ProductResponse])
def get_all_products(service: ProductService = Depends(get_product_service)):
    return service.get_all_products()
    
@router.post("/{product_id}/update")
def update_product(product_id: int, product: ProductUpdate,
                service: ProductService = Depends(get_product_service)):
    service.update_product(product_id, product)
    return "컨테이너 정보 수정이 완료되었습니다."
