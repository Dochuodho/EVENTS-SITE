#!/usr/bin/python3

from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine, Integer, String, Column

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer(),primary_key=True),
    name = Column(String())


    def __repr__(self):
        return f"User {self.name}, " +\
            f"is using an id of {self.id}"
    
class Event(Base):
    __tablename__ = 'events'
    id = Column(Integer(), primary_key=True),
    name = Column(String())
    location = Column(String()) 


    def __repr__(self):
        return f"Event is {self.name},"+\
            f"it will be held at {self.location}"
    
class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer(),primary_key=True),
    score = Column(Integer())


    def __repr__(self):
        return f"Your review is {self.score}"
    
    
    


