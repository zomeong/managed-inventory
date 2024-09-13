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

    def find_by_name(self, name: str):
        container = self.db.query(Container).filter(Container.name == name).first
        return container