from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.stock.stock_repository import StockRepository
from app.product.product_service import ProductService
from app.container.container_service import ContainerService
from app.transaction.transaction_schema import TransactionCreate
from app.models.models import TransactionType

class StockService:
    def __init__(self, db: Session):
        self.repository = StockRepository(db)
        self.product_service = ProductService(db)
        self.container_service = ContainerService(db)

    def create_stock(self, request: TransactionCreate):
        product = self.product_service.find_product_by_code(request.product_code)
        container = self.container_service.find_container_by_name(request.container_name)
        stock = self.repository.find_stock(product._id, container._id)

        if request.type == TransactionType.IN:
            if stock:
                self.repository.update(stock, request.quantity)
            else:
                self.repository.create(product._id, container._id, request.quantity)
        elif request.type == TransactionType.OUT:
            if stock and stock.quantity >= request.quantity:
                self.repository.update(stock, -request.quantity)
            else:
                raise HTTPException(status_code=400, detail="출고 수량이 재고 수량보다 많습니다.")
        
    def get_product_stock(self, id: int):
        self.product_service.find_product_by_id(id)
        stock_data = self.repository.find_by_product_id(id)
        total_stock = self.repository.sum_stock(id)

        return stock_data, total_stock
    
    def get_container_stock(self, id: int):
        self.container_service.find_container_by_id(id)
        return self.repository.find_by_container_id(id)