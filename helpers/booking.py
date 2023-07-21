from models.schema import User, Booking, session
from sqlalchemy.exc import IntegrityError
from flask import flash

booking_info = {}

def create_booking(owner_id, time):
    """Create a booking instance, and commit session to Booking table

    Args:
        owner_id: (Integer) id of the booking owner
        time: (String) A concatenated string of the day and time. It's important to highlight 
               that SQLAlchemy automatically converts a string to a DateTime type as long as the 
               column is of a DateTime.

    Raises IntegrityError           
    """
    try:
        """Because of the relationship we can access the user_id and reference it as owner_id"""
        user = User(user_id=owner_id) # First we need to get user object
        book = Booking(owner_id=user.user_id, date=time) 

        """Create the booking object so we can access it when email is being sent"""
        booking_info['id'] = book.booking_id
        booking_info['to'] = user.email
        booking_info['name'] = user.name

        session.add(book)
        session.commit()
    except IntegrityError:
        session.rollback()
        flash("There was an internal error. Please contact the admin.")    

def remove_booking(id):
    """Remove the booking by id
    
    Args:
        id: (Integer) id of the booking

    Raises IntegrityError    
    """
    try: 
        record = session.query(Booking).filter_by(booking_id=id).first()
        session.delete(record)
        session.commit()
    except IntegrityError:
        session.rollback()
        flash("User is owner of a booking. Please delete the booking first.")

def get_all_bookings():
    """Returns all the bookings
    Returns:
        results: (Booking)
    """
    results = session.query(Booking)
    return results

def get_booking(id):
    """Returns the booking object based on id
    Args:
        id: (Integer) id of the booking
    Returns:
        result: (Booking)
    """
    result = session.query(Booking).get(id)
    return result

def get_booking_owner(id):
    """Returns the booking owner based on owner_id

    Args:
        id: (Integer) id of the booking
    Returns:
        name: (User)
    """
    name = session.query(User).join(Booking, User.user_id).filter(Booking.owner_id==id)
    
    return name

def edit_booking(id, column, change):
    """Edit the bookings's information

    Args:
        id: (Integer) id of the booking to edit
        column: (String) Desired column to change
        change: (String) New value

        Raises IntegrityError
    """
    try:
        session.query(Booking).filter(id == id).update({column: change})
        session.commit()
    except IntegrityError:
        session.rollback()
        flash("User cannot be updated.")   

def get_bookings_by_user(id):
    """Returns a list of bookings based on owner_id
    Args:
        id: (Integer) id of the user
    Returns:
        bookings: (Booking)    
    """
    bookings = session.query(Booking).filter_by(owner_id=id).all()
    return bookings








