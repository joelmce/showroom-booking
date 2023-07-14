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


