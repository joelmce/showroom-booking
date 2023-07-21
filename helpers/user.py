from flask import flash
from sqlalchemy.exc import IntegrityError
from models.schema import User, session
from helpers.authenticate import hashpassword

def add_user(name, email, password, admin = False):
    """Adds the user to the User table

    By default the admin field is false in scenarios where the param is not parsed.

    Args:
        name: (String)
        email: (String)
        password: (String) Hashed
        admin: (Bool)

    Raises IntegrityError
    """
    try:
        hashed_password = hashpassword(password)
        user = User(name = name, email = email, password = hashed_password, admin = admin)
        session.add(user)
        session.commit()
    except IntegrityError:
        session.rollback()
        flash("User already exists!")    

def remove_user(id):
    """Removes the user from the User table.

    Args:
        id: (Integer) the id of the user

    Raises IntegrityError
    """
    try:
        record = session.query(User).filter_by(user_id=id).first()
        session.delete(record)
        session.commit()
    except IntegrityError:
        session.rollback()
        flash("User is owner of a booking. Please delete the booking first.")

def edit_user(id, column, change):
    """Edit the user's information

    Args:
        id: (Integer) id of the user to edit
        column: (String) Desired column to change
        change: (String) New value

        Raises IntegrityError
    """
    try:
        session.query(User).filter(id == id).update({column: change})
        session.commit()
    except IntegrityError:
        session.rollback()
        flash("User cannot be updated.")    
        

def get_user(name):
    """Return the user based on their name.

    Args:
        name: (String) name of the user

    Returns:
        user: (User)    
    """
    user = session.query(User).filter_by(name=name).first()
    return user

def get_user_by_id(id):
    """Get the user based on their id

    Args:
        id: (Integer) id of the user

    Returns:
        user: (User)        
    """
    user = session.query(User).filter_by(user_id=id).first()
    return user

def get_all():
    """Get all users in the User table"""
    results = session.query(User)
    return results


    