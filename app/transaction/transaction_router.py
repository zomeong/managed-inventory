from fastapi import APIRouter, Depends, HTTPException
from app.transaction.transaction_service import TransactionService
from app.transaction.transaction_schema import TransactionCreate, TransactionResponse
from sqlalchemy.orm import Session
from app.core.database import get_db
import logging
import traceback

router = APIRouter(
    prefix="/transactions",
)

def get_transaction_service(db: Session = Depends(get_db)):
    return TransactionService(db)

@router.post("")
def create_transaction(transaction: TransactionCreate, service: TransactionService = Depends(get_transaction_service)):
    try:
        service.create_transaction(transaction)
        return "입출고 기록이 추가되었습니다."

    except HTTPException as he:
        raise he    

    except Exception as e:
        logging.error(f"Unhandled exception: {str(e)}")
        logging.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail="서버 내부 오류가 발생하였습니다.")

@router.get("/{transaction_id}", response_model=TransactionResponse)
def get_transaction(transaction_id: int, service: TransactionService = Depends(get_transaction_service)):
    try:
        return service.get_transaction(transaction_id)

    except HTTPException as he:
        raise he    

    except Exception as e:
        logging.error(f"Unhandled exception: {str(e)}")
        logging.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail="서버 내부 오류가 발생하였습니다.")

@router.get("", response_model=list[TransactionResponse])
def get_all_transactions(service: TransactionService = Depends(get_transaction_service)):
    try:
        return service.get_all_transaction()

    except HTTPException as he:
        raise he    

    except Exception as e:
        logging.error(f"Unhandled exception: {str(e)}")
        logging.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail="서버 내부 오류가 발생하였습니다.")
