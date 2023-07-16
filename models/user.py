from sqlalchemy import create_engine, Column, Integer, String, Boolean, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('postgresql:///selectioncentre')
Session = sessionmaker(bind=engine)
session = Session()

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    admin = Column(Boolean) 

def add_user(name, email, password, admin = False):
    user = User(name = name, email = email, password = password, admin = admin)
    session.add(user)
    session.commit()

def remove_user(id):
    record = session.query.filter_by(id == id).one()
    session.delete(record)
    session.commit()

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


    