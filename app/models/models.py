from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum, BigInteger
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from enum import Enum as PyEnum

Base = declarative_base()

class TransactionType(str, PyEnum):
    IN = "입고"
    OUT = "출고"

class Product(Base):
    __tablename__ = "product"
    
    _id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String, nullable=False)
    
    # 관계 설정
    stock_items = relationship("Stock", back_populates="product")

class Container(Base):
    __tablename__ = "container"
    
    _id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    
    # 관계 설정
    stock_items = relationship("Stock", back_populates="container")

class Stock(Base):
    __tablename__ = "stock"
    
    _id = Column(BigInteger, primary_key=True, index=True)
    product_id = Column(BigInteger, ForeignKey("products.id"), nullable=False)
    container_id = Column(BigInteger, ForeignKey("containers.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    
    # 관계 설정
    product = relationship("Product", back_populates="stock_items")
    container = relationship("Container", back_populates="stock_items")

class Transaction(Base):
    __tablename__ = "transaction"
    
    _id = Column(BigInteger, primary_key=True, index=True)
    _type = Column(Enum(TransactionType), nullable=False)
    product_id = Column(BigInteger, nullable=False)
    container_id = Column(BigInteger, nullable=False)
    quantity = Column(Integer, nullable=False)
    date = Column(DateTime, nullable=False)
    manager_name = Column(String, nullable=True)