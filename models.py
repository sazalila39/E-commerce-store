from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class CouponTable(Base):
    __tablename__ = "coupons"
    id = Column(Integer, primary_key= True, autoincrement=True)
    code = Column(String(20),unique=True, nullable=False)
    discount = Column(Integer, nullable=False)

