import unittest

def add_numbers(x, y):
    return x + y

class TestAddition(unittest.TestCase):
    
    def test_addition(self):
        self.assertEqual(add_numbers(1, 2), 3)
        self.assertEqual(add_numbers(4, 5), 9)

if __name__ == '__main__':
    unittest.main()
