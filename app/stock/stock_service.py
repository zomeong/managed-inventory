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
                raise HTTPException(status_code=423, detail="출고 수량이 재고 수량보다 많습니다.")
        
    def get_product_stock(self, code: str):
        product = self.product_service.find_product_by_code(code)
        stock_data = self.repository.find_by_product_id(product._id)
        if len(stock_data) == 0:
            raise HTTPException(status_code=400, detail="재고가 존재하지 않습니다.")
        total_stock = self.repository.sum_stock(product._id)

        return stock_data, total_stock
    
    def get_container_stock(self, name: str):
        container = self.container_service.find_container_by_name(name)
        stock_data = self.repository.find_by_container_id(container._id)
        if len(stock_data) == 0:
            raise HTTPException(status_code=400, detail="재고가 존재하지 않습니다.")
        
        return stock_data
    
    def get_all_products_stock(self):
        stock_data = self.repository.get_all()

        stock_map = {}
        for stock in stock_data:
            product_code = stock.product_code
            container_name = stock.container_name
            quantity = stock.quantity

            if product_code not in stock_map:
                stock_map[product_code] = {
                    "total_stock" : 0,
                    "stock_data": []
                }
            
            stock_map[product_code]["total_stock"] += quantity
            stock_map[product_code]["stock_data"].append({
                "container_name": container_name,
                "quantity": quantity
            })

        return stock_map

    def get_all_containers_stock(self):
        stock_data = self.repository.get_all()

        stock_map = {}
        for stock in stock_data:
            product_code = stock.product_code
            container_name = stock.container_name
            quantity = stock.quantity

            if container_name not in stock_map:
                stock_map[container_name] = {
                    "total_stock" : 0,
                    "stock_data": []
                }
            
            stock_map[container_name]["total_stock"] += quantity
            stock_map[container_name]["stock_data"].append({
                "product_code": product_code,
                "quantity": quantity
            })

        return stock_map