import unittest
from src.main import square

class TestSquare(unittest.TestCase):
    def test_square(self):
        self.assertEqual(square(2), 4)
        self.assertEqual(square(-3), 9)

if __name__ == '__main__':
    unittest.main()
