import unittest
from solution import is_increasing
class IncreasingTest(unittest.TestCase):
	def test_increasing_seq(self):
		self.assertTrue(is_increasing([1,2,3,4,5]))
		self.assertTrue(is_increasing([1]))
	def test_not_increasing_seq(self):
		self.assertFalse(is_increasing([5,6,-10]))
		self.assertFalse(is_increasing([1,1,1,1]))
if __name__ == '__main__':
	unittest.main()
