import unittest
from solution import contains_digit
class DigitTest(unittest.TestCase):
	def test_contains(self):
		self.assertTrue(contains_digit(42, 2))
		self.assertTrue(contains_digit(1000, 0))
	def test_not_contains(self):
		self.assertTrue(not contains_digit(123, 4))
		self.assertTrue(not contains_digit(12346789, 5))

if __name__ == '__main__':
	unittest.main()
