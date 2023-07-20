from sqlalchemy import create_engine, Column, Integer, String, Boolean,DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

from dotenv import load_dotenv
import os
load_dotenv()

Base = declarative_base()
engine = create_engine(os.getenv('PRODUCTION_DB_URL'))

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    admin = Column(Boolean) 
    booking = relationship("Booking")

class Booking(Base):

    __tablename__ = 'bookings'

    booking_id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey('users.user_id'))
    date = Column(DateTime)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

