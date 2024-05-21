from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from jabama.model.entity.base import Base
from jabama.model.entity.person import Person
from jabama.model.entity.house import House

class Rent(Base):
    __tablename__ = "rent"
    id = Column(Integer, primary_key=True, autoincrement=True)
    house = Column(String(20), nullable=False)
    city = Column(String(20), nullable=False)
    customer = Column(String(20), nullable=False)
    price=Column(String)
    #datetime=

    def __init__(self, id, house, city, customer, price, datetime):
        self.id = id
        self.house = house
        self.city = city
        self.customer = customer
        self.price = price
        self.datetime = datetime


