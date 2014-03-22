import unittest
from solution import sum_of_digits
class SumDigitsTest(unittest.TestCase):
	def test_big_number(self):
		self.assertEqual(43,sum_of_digits(1325132435356))
	def test_123(self):
		self.assertEqual(6,sum_of_digits(123))
	def test_6(self):
		self.assertEqual(6,sum_of_digits(6))
	def test_negative_num(self):
		self.assertEqual(1,sum_of_digits(-10))

if __name__ == '__main__':
	unittest.main()
