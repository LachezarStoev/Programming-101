import unittest
from solution import prime_number_of_divisors
class NumberOfDivisorTest(unittest.TestCase):
	def test_prime(self):
		self.assertTrue(prime_number_of_divisors(7))
		self.assertTrue(prime_number_of_divisors(9))
	def test_not_prime(self):
		self.assertTrue(not prime_number_of_divisors(8))

if __name__ == '__main__':
	unittest.main()
