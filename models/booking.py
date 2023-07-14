from sqlalchemy import create_engine, Column, Integer, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from user import User

Base = declarative_base()
engine = create_engine('postgresql:///selectioncentre')
Session = sessionmaker(bind=engine)
session = Session()

class Booking(Base):

    __tablename__ = 'bookings'

    booking_id = Column(Integer, primary_key=True)
    owner_id = Column(
        Integer,
        ForeignKey('users.user_id', ondelete='CASCADE'),
        nullable=False
    )

    date = Column(DateTime)

    owner = relationship('User', backref='bookings')

def create_booking(owner_id, time):
    u = User(user_id=owner_id)
    b = Booking(owner_Id=u.user_id, date=time)
    session.add(b)

def delete_booking(id):
    record = Booking.query.filter_by(Booking.booking_id == id).one()
    session.delete(record)
    session.commit()

def get_all_bookings():
    results = session.query(Booking)
    return results

def get_booking(id):
    result = session.query(Booking).get(id)
    return result







