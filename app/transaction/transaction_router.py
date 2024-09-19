from fastapi import APIRouter, Query, Depends
from app.transaction.transaction_service import TransactionService
from sqlalchemy.orm import Session
from app.core.database import get_db

router = APIRouter(
    prefix="/transactions",
)

def get_transaction_service(db: Session = Depends(get_db)):
    return TransactionService(db)


