import unittest

# Example function to test
def add_numbers(a, b):
    return a + b

# Test class
class TestAddNumbers(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(add_numbers(2, 3), 5)

    def test_add_negative(self):
        self.assertEqual(add_numbers(-1, -2), -3)

    def test_add_zero(self):
        self.assertEqual(add_numbers(0, 0), 0)

if __name__ == "__main__":
    unittest.main()  # Ensures that the tests will run when this script is executed
