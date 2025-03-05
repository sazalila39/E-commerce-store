import random
import string
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine("", echo=True)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


class CouponTable(Base):
    __tablename__ = "coupons"
    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String(20), unique=True, nullable=False)
    discount = Column(Integer, nullable=False)


Base.metadata.create_all(engine)


def seed_table():
    session = SessionLocal()

    session.bulk_save_objects([CouponTable(code=''.join(random.choices(string.ascii_uppercase + string.digits, k=10)), discount=random.randint(1,100)) for _ in range(1000)])
    session.commit()
    session.close()
    print("1000 coupons added")


if __name__ == "__main__":
    seed_table()

