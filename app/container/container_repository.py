from sqlalchemy.orm import Session
from app.models.models import Container

class ContainerRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, createReq):
        container = Container(**createReq.dict())
        self.db.add(container)
        self.db.commit()
        self.db.refresh(container)

    def get_all(self):
        return self.db.query(Container).all()

    def find_by_name(self, name: str):
        return self.db.query(Container).filter(Container.name == name).first()
    
    def find_by_id(self, id: int):
        return self.db.query(Container).filter(Container._id == id).first()