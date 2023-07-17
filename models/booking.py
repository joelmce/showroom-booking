from models.schema import User, Booking, session

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

def get_bookings_by_user(id):
    bookings = session.query(Booking).filter_by(owner_id=id).all()
    return bookings








