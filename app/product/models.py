from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum, BigInteger
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from enum import Enum as PyEnum
from app.database import Base



class Product(Base):
    __tablename__ = "product"
    
    _id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String, nullable=False)
    code = Column(String, nullable=False, unique=True)
    
    # 관계 설정
    stock_items = relationship("Stock", back_populates="product")
