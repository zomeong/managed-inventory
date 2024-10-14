from fastapi import APIRouter, Depends, FastAPI
from app.transaction.transaction_service import TransactionService
from app.transaction.transaction_schema import TransactionCreate, TransactionResponse
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.exception_handler import exception_handler

app = FastAPI()
router = APIRouter(
    prefix="/transactions",
)

def get_transaction_service(db: Session = Depends(get_db)):
    return TransactionService(db)

@router.post("",
    description="""
    입출고 기록 추가 API<br>
    * id: 자동 생성<br>
    * date: create시 현재 시간으로 자동 할당

    Input
    - type: 분류(입고/출고)
    - product_code: 물품 코드
    - container_name: 창고 이름
    - quantity: 입/출고 수량
    """)
@exception_handler
def create_transaction(transaction: TransactionCreate, service: TransactionService = Depends(get_transaction_service)):
    service.create_transaction(transaction)
    return "입출고 기록이 추가되었습니다."

@router.get("/{transaction_id}", response_model=TransactionResponse, description="입출고 기록 조회 API")
@exception_handler
def get_transaction(transaction_id: int, service: TransactionService = Depends(get_transaction_service)):
    return service.get_transaction(transaction_id)

@router.get("", response_model=list[TransactionResponse], description="전체 입출고 기록 조회 API")
@exception_handler
def get_all_transactions(service: TransactionService = Depends(get_transaction_service)):
    return service.get_all_transaction()