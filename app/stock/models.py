from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum, BigInteger
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from enum import Enum as PyEnum
from app.database import Base


class Stock(Base):
    __tablename__ = "stock"
    
    _id = Column(BigInteger, primary_key=True, index=True)
    product_id = Column(BigInteger, ForeignKey("product._id"), nullable=False)
    # container_id = Column(BigInteger, ForeignKey("container._id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    
    # 관계 설정
    product = relationship("Product", back_populates="stock_items")
    # container = relationship("Container", back_populates="stock_items")
