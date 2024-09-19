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
        product = self.find_product(id)
        return product
    
    def get_all_products(self):
        return self.repository.get_all()
    
    def update_product(self, id: int, request: ProductUpdate):
        product = self.find_product(id)
        self.check_code(request.code)
        self.check_name(request.name)
        self.repository.update(product, request)

    def find_product(self, id:int):
        product = self.repository.find_by_id(id)
        if product is None:
            raise HTTPException(status_code=404, detail="물품을 찾을 수 없습니다")
        return product
    
    def check_name(self, name:str):
        product = self.repository.find_by_name(name)
        if product:
            raise HTTPException(status_code=400, detail="이미 존재하는 상품 이름입니다.")

    def check_code(self, code:str):
        product = self.repository.find_by_code(code)
        if product:
            raise HTTPException(status_code=400, detail="이미 존재하는 상품 코드입니다.")