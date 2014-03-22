import unittest
from solution import contains_digits
class AllDigitsTest(unittest.TestCase):
	def test_contains(self):
		self.assertTrue(contains_digits(402123, [0, 3, 4]))
		self.assertTrue(contains_digits(456, []))
	def test_not_contains(self):
		self.assertTrue(not contains_digits(666, [6,4]))
		self.assertTrue(not contains_digits(123456789, [1,2,3,0]))

if __name__ == '__main__':
	unittest.main()
