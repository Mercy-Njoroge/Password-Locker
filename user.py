class User:
    '''
    Class that generates instances of user accounts
    '''
    user_list = []
    def __init__(self, user_name, user_password):
        '''
        __init__ method to define the properties of a User object

        Args:
        user_name : name of a user
        user_password : password for a user
       '''

        self.user_name = user_name
        self.user_password = user_password