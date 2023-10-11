import unittest
from app import app

# Create a test class that inherits from unittest.TestCase
class TestIsEven(unittest.TestCase):

    # Each test method should start with "test_"
    
    def true_when_x_is_17(self):
        self.assertTrue(app.is_prime(4), "True")

    def false_when_x_is_36(self):
        self.assertFalse(app.is_prime(36), "False")
        
    def true_when_x_is_13219(self):
        self.assertFalse(app.is_prime(13219), "False")

if __name__ == '__main__':
    unittest.main()

