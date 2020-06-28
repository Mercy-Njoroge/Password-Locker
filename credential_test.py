import unittest
from credential import Credential

class TestCredential(unittest.TestCase):
    '''
    Test class that defines test cases for the Credential Class behaviours

    Args:
        unittest.TestCase : Test case class that helps create test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test case
        '''

        # Create credential object
        self.new_credential = Credential("Nyugi","Gmail","kenya1")

    def tearDown(self):
        '''
        tearDown method that cleans up after each test case is run
        '''

        Credential.credential_list = []

    def test_init(self):
        '''
        Test case to test if the object is initialised properly
        '''
        self.assertEqual( self.new_credential.user_password, "Nyugi")
        self.assertEqual( self.new_credential.credential_name, "Gmail" )
        self.assertEqual( self.new_credential.credential_password, "kenya1" )

    def test_save_credential(self):
        '''
        Test case to test if the user object is saved into the user list
        '''

    
        self.new_credential.save_credential()

        self.assertEqual( len(Credential.credential_list), 1 )