from sqlalchemy.orm import Session
from app.models.models import Transaction

class TransactionRepository:
    def __init__(self, db: Session):
        self.db = db
