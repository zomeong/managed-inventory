from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.transaction.transaction_schema import TransactionCreate
from app.transaction.transaction_repository import TransactionRepository
from app.product.product_repository import ProductRepository
from app.container.container_repository import ContainerRepository
from app.stock.stock_service import StockService

class TransactionService:
    def __init__(self, db: Session):
        self.repository = TransactionRepository(db)
        self.product_repository = ProductRepository(db)
        self.container_repository = ContainerRepository(db)
        self.stock_service = StockService(db)

    def create_transaction(self, request: TransactionCreate):
        self.stock_service.create_stock(request)
        self.repository.create(request)

    def get_transaction(self, id: int):
        return self.find_transaction(id)
    
    def get_all_transaction(self):
        return self.repository.get_all()

    def find_transaction(self, id: int):
        transaction = self.repository.find_by_id(id)
        if transaction is None:
            raise HTTPException(status_code=404, detail="입출고 기록을 찾을 수 없습니다")
        return transaction