from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from jabama.model.entity.base import Base
from jabama.model.entity.person import Person

class House(Base):
    __tablename__ = "house"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    city = Column(String(20), nullable=False)
    meterage = Column(Integer)
    #address = Column(String())
    finalladress=Column(String)
    plate=Column(String(5))
    numberofrooms = Column(Integer, default=0)
    elevator = Column(Boolean, default=False)
    parking = Column(Boolean, default=False)
    warehouse = Column(Boolean, default=False)
    price=Column(String)
    house_id = Column(Integer, ForeignKey("person.id"))
    house = relationship(Person)



    def __init__(self, id, name, city ,meterage ,address,finalladress, plate, numberofrooms,elevator,parking,warehouse,price):
        self.id = id
        self.name = name
        self.city = city
        self.meterage = meterage
        self.address = address
        self.finalladress =finalladress
        self.plate = plate
        self.numberofrooms=numberofrooms
        self.elevator =elevator
        self.parking = parking
        self.warehouse = warehouse
        self.price = price

