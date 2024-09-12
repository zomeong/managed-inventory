from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .schemas import Product, ProductCreate, ProductUpdate
from .service import ProductService
from ..database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.get("/products/", response_model=list[Product])
def get_products(db: Session = Depends(get_db)):
    crud = ProductService(db)
    return crud.get_products()

@router.get("/products/{product_id}", response_model=Product)
def get_product(product_id: int, db: Session = Depends(get_db)):
    crud = ProductService(db)
    db_product = crud.get_product(product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@router.post("/products/", response_model=Product)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    crud = ProductService(db)
    return crud.create_product(product)

@router.put("/products/{product_id}", response_model=Product)
def update_product(product_id: int, product: ProductUpdate, db: Session = Depends(get_db)):
    crud = ProductService(db)
    db_product = crud.update_product(product_id, product)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@router.delete("/products/{product_id}", response_model=Product)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    crud = ProductService(db)
    db_product = crud.delete_product(product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product