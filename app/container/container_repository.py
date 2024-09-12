from sqlalchemy.orm import Session

class ContainerRepository:
    def __init__(self, db: Session):
        self.db = db