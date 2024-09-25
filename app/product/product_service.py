from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.product.product_repository import ProductRepository
from app.product.product_schema import ProductCreate, ProductUpdate

class ProductService:
    def __init__(self, db: Session):
        self.repository = ProductRepository(db)

    def create_product(self, request: ProductCreate):
        self.check_code(request.code)
        self.check_name(request.name)
        self.repository.create(request)

    def get_product(self, id:int):
        return self.find_product_by_id(id)
    
    def get_all_products(self):
        return self.repository.get_all()
    
    def search_products_by_name(self, name: str):
        return self.repository.search_by_name(name)
    
    def search_products_by_code(self, code: str):
        return self.repository.search_by_code(code)

    def update_product(self, id: int, request: ProductUpdate):
        product = self.find_product_by_id(id)
        self.check_code(request.code)
        self.check_name(request.name)
        self.repository.update(product, request)

    def find_product_by_id(self, id:int):
        product = self.repository.find_by_id(id)
        if product is None:
            raise HTTPException(status_code=404, detail="물품을 찾을 수 없습니다")
        return product
    
    def find_product_by_code(self, code: str):
        product = self.repository.find_by_code(code)
        if product is None:
            raise HTTPException(status_code=404, detail="물품을 찾을 수 없습니다.")
        return product

    def check_name(self, name:str):
        product = self.repository.find_by_name(name)
        if product:
            raise HTTPException(status_code=400, detail="이미 존재하는 물품 이름입니다.")

    def check_code(self, code:str):
        product = self.repository.find_by_code(code)
        if product:
            raise HTTPException(status_code=400, detail="이미 존재하는 물품 코드입니다.")