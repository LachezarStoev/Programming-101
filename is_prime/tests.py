import unittest
from solution import is_prime
class PrimeTest(unittest.TestCase):
	def test_numbers_prime(self):
		self.assertTrue(is_prime(2))
		self.assertTrue(is_prime(11))
	def test_numbers_not_prime(self):
		self.assertTrue(not is_prime(1))
		self.assertTrue(not is_prime(8))
		self.assertTrue(not is_prime(-10))

if __name__ == '__main__':
	unittest.main()
