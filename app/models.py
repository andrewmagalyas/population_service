from sqlalchemy import Column, Integer, String, BigInteger
from app.database import Base

class Country(Base):
    __tablename__ = "countries"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    name = Column(String, index=True)
    region = Column(String, index=True)
    population = Column(BigInteger)
