from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .schemas import Stock
from .service import StockService
from ..database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
     
@router.get("/products/stock/", response_model=list[Stock])
def get_stocks(db: Session = Depends(get_db)):
    service = StockService(db)
    return service.get_stocks()

@router.get("/products/{product_id}/stock/", response_model=Stock)
def get_stock(product_id: int, db: Session = Depends(get_db)):
    service = StockService(db)
    db_stock = service.get_stock(product_id)
    if db_stock is None:
        raise HTTPException(status_code=404, detail="Stock not found")
    return db_stock