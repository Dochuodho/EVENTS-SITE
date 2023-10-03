#!/usr/bin/python3

from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from sqlalchemy import create_engine, Integer, String, Column, ForeignKey

Base = declarative_base()

user_event = Table (
    'user_event',
    Base.metadata,
    Column('user_id',ForeignKey('users.id'),primary_key=True),
    Column('event_id', ForeignKey('events.id'),primary_key=True) ,
    extend_existing=True
)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer(),primary_key=True),
    name = Column(String())
    event = relationship("Event",secondary=user_event,back_populates=backref('users'))
    review = relationship("Review",backref=backref('users'))

 
    def __repr__(self):
        return f"User {self.name}, " +\
            f"is using an id of {self.id}"
     
class Event(Base):
    __tablename__ = 'events'
    id = Column(Integer(), primary_key=True),
    name = Column(String())
    location = Column(String()) 
    user = relationship("User",secondary=user_event,back_populates=backref('events'))
    review = relationship("Event",backref=backref('events'))


    def __repr__(self):
        return f"Event is {self.name},"+\
            f"it will be held at {self.location}"
    
class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer(),primary_key=True),
    score = Column(Integer())
    user_id = Column(Integer(), ForeignKey("users.id"))
    event_id = Column(Integer(), ForeignKey("events.id"))



    def __repr__(self):
        return f"Your review is {self.score}"
    
if __name__ == "__main__":
    engine = create_engine('sqlite://my_database.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    



    
    
    


