from functools import wraps
from flask import abort, session, redirect, flash
from sqlalchemy.orm.exc import NoResultFound
import bcrypt

def login_required(f):
    '''A class decorator that checks if the user is an admin, which returns the wrapped function if true
    '''
    @wraps(f)
    def func(*args, **kwargs):
        user_perm = session.get('admin', '')
        if user_perm:
            return f(*args, **kwargs)
        return abort(401)
    return func      

def hashpassword(password):
    """Hash a password
    Returns:
        An encrypted password
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

def checkpassword(user, entered_password):
    """Compare two passwords from the name and the password they entered

    Returns:
        password_check: (Bool) Result of comparison
    """
    password_check = bcrypt.checkpw(entered_password.encode(), user.password.encode())
    return password_check

def login_user(fetched_user, password):
    '''Login the user

    TODO: Is it wise to handle the password hashing here or at the source?

    Args: the id assigned to the user

    Returns:
        A boolean if the login has been successful or not.
    '''
    try:
        if fetched_user is not None:
            #checkpassword(fetched_user, password)
            if password == fetched_user.password:
                session['user'] = fetched_user.name
                session['admin'] = fetched_user.admin
            else:
                flash("Password is incorrect")
                return False
    except NoResultFound:
        flash("User does not exist")
        return False