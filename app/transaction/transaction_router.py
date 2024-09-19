from fastapi import APIRouter, Depends
from app.transaction.transaction_service import TransactionService
from app.transaction.transaction_schema import TransactionBase, ResponseTransaction
from sqlalchemy.orm import Session
from app.core.database import get_db

router = APIRouter(
    prefix="/transactions",
)

def get_transaction_service(db: Session = Depends(get_db)):
    return TransactionService(db)

@router.post("")
def create_transaction(transaction: TransactionBase, service: TransactionService = Depends(get_transaction_service)):
    service.create_transaction(transaction)
    return "입출고 기록이 추가되었습니다."

@router.get("/{transaction_id}", response_model=ResponseTransaction)
def get_transaction(transaction_id: int, service: TransactionService = Depends(get_transaction_service)):
    return service.get_transaction(transaction_id)

@router.get("", response_model=list[ResponseTransaction])
def get_all_transactions(service: TransactionService = Depends(get_transaction_service)):
    return service.get_all_transaction()
