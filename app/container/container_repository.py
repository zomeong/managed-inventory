from sqlalchemy.orm import Session
from sqlalchemy import or_
from app.models.models import Container

class ContainerRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, request):
        container = Container(**request.dict())
        self.db.add(container)
        self.db.commit()
        self.db.refresh(container)

    def update(self, container, request):
        for key, value in request.dict().items():
            if value is not None:
                setattr(container, key, value)
        self.db.commit()
        self.db.refresh(container)

    def get_all(self):
        return self.db.query(Container).all()
    
    def find_by_id(self, id: int):
        return self.db.query(Container).filter(Container._id == id).first()

    def find_by_name(self, name: str):
        return self.db.query(Container).filter(Container.name == name).first()
    
    def search_by_name(self, name: str):
        return self.db.query(Container).filter(
            or_(
                Container.name == name,
                Container.name.ilike(f"%{name}%")
            )
        ).all()