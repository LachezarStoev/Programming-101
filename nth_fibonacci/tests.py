import unittest
from solution import nth_fibonacci

class FibonacciTest(unittest.TestCase):
	def test_fibonacci_negative(self):
		self.assertEqual("Error!",nth_fibonacci(-1))
		self.assertEqual("Error!",nth_fibonacci(0))
	def test_fibonacci_one(self):
		self.assertEqual(1,nth_fibonacci(1))
	def test_fibonacci_5(self):
		self.assertEqual(5,nth_fibonacci(5))

if __name__ == '__main__':
	unittest.main()
