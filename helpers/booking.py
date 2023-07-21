from models.schema import User, Booking, session
from sqlalchemy.exc import IntegrityError
from flask import flash

def create_booking(owner_id, time):
    u = User(user_id=owner_id)
    b = Booking(owner_id=u.user_id, date=time)
    session.add(b)
    session.commit()

def remove_booking(id):
    try: 
        record = session.query(Booking).filter_by(booking_id=id).first()
        session.delete(record)
        session.commit()
    except IntegrityError:
        session.rollback()
        flash("User is owner of a booking. Please delete the booking first.")

def get_all_bookings():
    results = session.query(Booking)
    return results

def get_booking(id):
    result = session.query(Booking).get(id)
    return result

def get_booking_owner(id):
    name = session.query(User).join(Booking, User.user_id).filter(Booking.user_id==id)
    return name

def get_bookings_by_user(id):
    bookings = session.query(Booking).filter_by(owner_id=id).all()
    return bookings








