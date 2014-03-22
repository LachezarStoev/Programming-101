import unittest
from solution import is_decreasing
class DecreasingTest(unittest.TestCase):
	def test_decreasing_seq(self):
		self.assertTrue(is_decreasing([5,4,3,2,1]))
		self.assertTrue(is_decreasing([100, 50, 20]))
	def test_not_decreasing_seq(self):
		self.assertFalse(is_decreasing([1,2,3]))
		self.assertFalse(is_decreasing([1,1,1,1]))
if __name__ == '__main__':
	unittest.main()
