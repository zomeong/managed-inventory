from fastapi import APIRouter, Depends, HTTPException
from app.product.product_service import ProductService
from app.product.product_schema import ProductCreate, ProductUpdate, ProductResponse
from sqlalchemy.orm import Session
from app.core.database import get_db
import logging
import traceback

router = APIRouter(
    prefix="/products",
)

def get_product_service(db: Session = Depends(get_db)):
    return ProductService(db)

@router.post("")
def create_product(product: ProductCreate, service: ProductService = Depends(get_product_service)):
    try:
        service.create_product(product)
        return "물품 생성이 완료되었습니다."
    
    except HTTPException as he:
        raise he    

    except Exception as e:
        logging.error(f"Unhandled exception: {str(e)}")
        logging.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail="서버 내부 오류가 발생하였습니다.")

@router.get("/{product_id}", response_model=ProductResponse)
def get_product(product_id:int, service: ProductService = Depends(get_product_service)):
    try:
        return service.get_product(product_id)

    except HTTPException as he:
        raise he    

    except Exception as e:
        logging.error(f"Unhandled exception: {str(e)}")
        logging.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail="서버 내부 오류가 발생하였습니다.")

@router.get("", response_model=list[ProductResponse])
def get_all_products(service: ProductService = Depends(get_product_service)):
    try:
        return service.get_all_products()
    
    except HTTPException as he:
        raise he    

    except Exception as e:
        logging.error(f"Unhandled exception: {str(e)}")
        logging.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail="서버 내부 오류가 발생하였습니다.")
    
@router.get("/search/name/{product_name}", response_model=list[ProductResponse])
def search_products_by_name(product_name: str, service: ProductService = Depends(get_product_service)):
    try:
        return service.search_products_by_name(product_name)
    
    except HTTPException as he:
        raise he    

    except Exception as e:
        logging.error(f"Unhandled exception: {str(e)}")
        logging.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail="서버 내부 오류가 발생하였습니다.")

@router.get("/search/code/{product_code}", response_model=list[ProductResponse])
def search_products_by_code(product_code: str, service: ProductService = Depends(get_product_service)):
    try:
        return service.search_products_by_code(product_code)

    except HTTPException as he:
        raise he    

    except Exception as e:
        logging.error(f"Unhandled exception: {str(e)}")
        logging.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail="서버 내부 오류가 발생하였습니다.")

@router.post("/{product_id}/update")
def update_product(product_id: int, product: ProductUpdate,
                service: ProductService = Depends(get_product_service)):
    try:
        service.update_product(product_id, product)
        return "컨테이너 정보 수정이 완료되었습니다."

    except HTTPException as he:
        raise he    

    except Exception as e:
        logging.error(f"Unhandled exception: {str(e)}")
        logging.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail="서버 내부 오류가 발생하였습니다.")
