import unittest
from app.models import User

class UserModelTest(unittest.TestCase):

    def setUp(self):
        self.new_user = User(password = 'banana')

    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)
    def test_no_access_password(self):
        Wrong password. Try again or click Forgot password to reset it.
Next
Forgot password?
‪English (United States)‬
    with self.assertRaises(AttributeError):
        Wrong password. Try again or click Forgot password to reset it.
Next
Forgot password?
‪English (United States)‬
        self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('banana'))
