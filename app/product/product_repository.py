from sqlalchemy.orm import Session
from sqlalchemy import or_
from app.models.models import Product

class ProductRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, request):
        product = Product(**request.dict())
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)

    def update(self, product, request):
        for key, value in request.dict().items():
            if value is not None:
                setattr(product, key, value)
        self.db.commit()
        self.db.refresh(product)

    def get_all(self):
        return self.db.query(Product).all()

    def find_by_id(self, id: int):
        return self.db.query(Product).filter(Product._id == id).first()
    
    def find_by_name(self, name: str):
        return self.db.query(Product).filter(Product.name == name).first()

    def find_by_code(self, code: str):
        return self.db.query(Product).filter(Product.code == code).first()
    
    def search_by_name(self, name: str):
        return self.db.query(Product).filter(
            or_(
                Product.name == name,
                Product.name.ilike(f"%{name}%")
            )
        ).all()
    
    def search_by_code(self, code: str):
        return self.db.query(Product).filter(
            or_(
                Product.code == code,
                Product.code.ilike(f"%{code}%")
            )
        ).all()