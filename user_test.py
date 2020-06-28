import unittest
from user import User


class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the User Class behaviours

    Args:
        unittest.TestCase : Test case class that helps create test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test case
        '''

        self.new_user = User("James","Nyugi")


    def tearDown(self):
        '''
        tearDown method that cleans up after each test case is run
        '''
        User.user_list = []


    def test_init(self):
        '''
        Test case to test if the object is initialised properly
        '''

        self.assertEqual( self.new_user.user_name, "James" )
        self.assertEqual( self.new_user.user_password, "Nyugi" )

    def test_save_user(self):
        '''
        Test case to test if the user object is saved into the user list
        '''
        self.new_user.save_user()

        self.assertEqual( len(User.user_list), 1 )

    def test_save_multiple_users(self):
        '''
        Test case to test if you can save multiple objects to user list
        '''

        self.new_user.save_user()

        test_user = User("Jossie","Ngat")

        test_user.save_user()

        self.assertEqual( len(User.user_list), 2)


if __name__ ==  '__main__':
    unittest.main()