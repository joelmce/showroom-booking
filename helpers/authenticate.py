from functools import wraps
from flask import abort, session

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

def register_user() -> bool:
    '''Registers the user

    Args: the id assigned to the user

    Returns:
        A boolean if the registration has failed or not.

    Raises:
        AuthError: There was an error with registering the user            
    '''
    pass

def login_user() -> bool:
    '''Login the user

    TODO: Is it wise to handle the password hashing here or at the source?

    Args: the id assigned to the user

    Returns:
        A boolean if the login has been successful or not.
    '''
    pass

def logout_user() -> bool:
    '''Logout the user
    This will simply clear the session cache of the browser.

    Returns:
        A boolean if the logout has succeeded. 
    '''
    pass

def is_admin() -> bool:
    pass


