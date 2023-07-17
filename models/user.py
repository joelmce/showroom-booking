from flask import flash
from sqlalchemy.exc import IntegrityError
from models.schema import User, session

def add_user(name, email, password, admin = False):
    try:
        user = User(name = name, email = email, password = password, admin = admin)
        session.add(user)
        session.commit()
    except IntegrityError:
        session.rollback()
        flash("User already exists!")    

def remove_user(id):
    try:
        record = session.query(User).filter_by(user_id=id).first()
        session.delete(record)
        session.commit()
    except IntegrityError:
        session.rollback()
        flash("User is owner of a booking. Please delete the booking first.")

def edit_user(id, change, **columns):
    for col in columns:
        session.query(User).filter(id == id).update({col: change})
        session.commit()

def get_user(name):
    user = session.query(User).filter_by(name=name).first()
    return user

def get_all():
    results = session.query(User)
    return results


    