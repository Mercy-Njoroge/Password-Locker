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

        def test_init(self):
        '''
        Test case to test if the object is initialised properly
        '''

        self.assertEqual( self.new_user.user_name, "James" )
        self.assertEqual( self.new_user.user_password, "Nyugi" )
