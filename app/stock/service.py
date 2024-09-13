from sqlalchemy.orm import Session
from .models import Stock
from . import schemas
from app.transaction.models import Transaction, TransactionType

class StockService:
    def __init__(self, db:Session):
        self.db = db
    
    # 재고 전체 조회
    def get_stocks(self):
        return self.db.query(Stock).all()
    
    # 특정 재고 조회
    def get_stock(self, product_id: int):
        return self.db.query(Stock).filter(Stock.product_id == product_id).first()

    # 재고 업데이트
    def update_stock(self, transaction_id: int):
        # 거래 기록을 조회
        transaction = self.db.query(Transaction).filter(Transaction._id == transaction_id).first()
        if not transaction:
            raise ValueError("Transaction not found")

        # 모든 재고를 조회
        stocks = self.get_stock(transaction.product_id)
        
        # 거래의 유형에 따라 재고 업데이트
        if transaction._type == TransactionType.IN:
            for stock in stocks:
                if stock.container_id == transaction.container_id:
                    stock.quantity += transaction.quantity
                    break
            else:
                if transaction.quantity > 0:
                    new_stock = Stock(
                        product_id=transaction.product_id,
                        container_id=transaction.container_id,
                        quantity=transaction.quantity
                    )
                    self.db.add(new_stock)
        elif transaction._type == TransactionType.OUT:
            for stock in stocks:
                if stock.container_id == transaction.container_id:
                    new_quantity = stock.quantity - transaction.quantity
                    if new_quantity < 0:
                        raise ValueError("Stock quantity cannot be negative")
                    stock.quantity = new_quantity
                    break
            else:
                raise ValueError("Cannot reduce stock below zero for a non-existing entry")

        self.db.commit()
        for stock in stocks:
            self.db.refresh(stock)
        return stocks