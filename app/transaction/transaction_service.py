from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.transaction.transaction_repository import TransactionRepository

class TransactionService:
    def __init__(self, db: Session):
        self.repository = TransactionRepository(db)