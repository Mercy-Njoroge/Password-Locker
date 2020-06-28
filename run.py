from user import User
from credential import Credential

def create_user(name, password):
    '''
    Function to create a user account

    Args:
        name : the name the user wants for the account
        password : the password the user want for the account
    '''

    new_user = User(name,password)

    return new_user

def save_users(user):
    '''
    Function to save a user account

    Args:
        user : the user account to be saved
    '''

    user.save_user()

def check_existing_users(name):
    '''
    Function that checks if a user account name already exists

    Args:
        name : the user account name
    '''

    return User.user_exist(name)