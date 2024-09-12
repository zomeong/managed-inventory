from sqlalchemy.orm import Session
from . import models, schemas

class ProductService:
    def __init__(self, db:Session):
        self.db = db
    
    # 물품 전체 조회
    def get_products(self):
        return self.db.query(models.Product).all()
    
    # 물품 정보 조회 
    def get_product(self, product_id: int):
        return self.db.query(models.Product).filter(models.Product._id == product_id).first()
    
    # 물품 등록
    def create_product(self, product: schemas.ProductCreate):
        db_product = models.Product(**product.dict())
        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return db_product
    
    # 물품 정보 수정
    def update_product(self, product_id: int, product:schemas.ProductUpdate):
        db_product = self.get_product(product_id)
        if db_product:
            for key, value in product.dict().items():
                setattr(db_product, key, value)
            self.db.commit()
            self.db.refresh(db_product)
        return db_product
    
    # 물품 삭제
    def delete_product(self, product_id: int):
        db_product = self.get_product(product_id)
        if db_product:
            self.db.delete(db_product)
            self.db.commit()
        return db_product
    
    
    
                
