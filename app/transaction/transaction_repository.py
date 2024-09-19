from sqlalchemy.orm import Session
from app.models.models import Transaction

class TransactionRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, request):
        transaction = Transaction(**request.dict())
        self.db.add(transaction)
        self.db.commit()
        self.db.refresh(transaction)

    def get_all(self):
        return self.db.query(Transaction).all()

    def find_by_id(self, id: int):
        return self.db.query(Transaction).filter(Transaction._id == id).first()