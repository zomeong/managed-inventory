from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.models import Stock, Product, Container

class StockRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, product_id: int, container_id: int, quantity: int):
        stock = Stock(product_id=product_id, container_id=container_id, quantity=quantity)
        self.db.add(stock)
        self.db.commit()
        self.db.refresh(stock)

    def update(self, stock: Stock, quantity: int):
        stock.quantity += quantity
        self.db.commit()
        self.db.refresh(stock)
        
    def find_stock(self, product_id: int, container_id: int):
        return self.db.query(Stock).filter(Stock.product_id == product_id, Stock.container_id == container_id).first()

    def find_by_product_id(self, id: int):
        return self.db.query(
            Container.name.label("container_name"),
            Stock.quantity
        ).join(Container).filter(Stock.product_id == id).all()
    
    def find_by_container_id(self, id: int):
        return self.db.query(
            Product.code.label("product_code"),
            Stock.quantity
        ).join(Product).filter(Stock.container_id == id).all()
    
    def get_all(self):
        return (
            self.db.query(
                Product.code.label("product_code"),
                Container.name.label("container_name"),
                Stock.quantity
            )
            .join(Stock, Stock.product_id == Product._id)
            .join(Container, Stock.container_id == Container._id)
            .all()
        )

    def sum_stock(self, id: int):
        return self.db.query(func.sum(Stock.quantity)).filter(Stock.product_id == id).scalar()
    