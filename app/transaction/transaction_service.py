from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.transaction.transaction_schema import TransactionCreate
from app.transaction.transaction_repository import TransactionRepository
from app.product.product_repository import ProductRepository
from app.container.container_repository import ContainerRepository

class TransactionService:
    def __init__(self, db: Session):
        self.repository = TransactionRepository(db)
        self.product_repository = ProductRepository(db)
        self.container_repository = ContainerRepository(db)

    def create_transaction(self, request: TransactionCreate):
        self.check_product(request.product_code)
        self.check_container(request.container_name)
        # todo : 재고 로직
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

    def check_product(self, code:str):
        product = self.product_repository.find_by_code(code)
        if product is None:
            raise HTTPException(status_code=404, detail="존재하지 않는 상품 코드입니다.")
        
    def check_container(self, name:str):
        container = self.container_repository.find_by_name(name)
        if container is None:
            raise HTTPException(status_code=404, detail="존재하지 않는 창고입니다.")