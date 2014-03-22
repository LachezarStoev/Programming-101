import unittest
from solution import sevens_in_a_row
class SevensTest(unittest.TestCase):
	def test_more_sevens(self):
		self.assertTrue(sevens_in_a_row([10,8,7,6,7,7,7,20,-7], 3))
		self.assertTrue(sevens_in_a_row([7,7,7,1,1,1,7,7,7,7], 3))
		self.assertTrue(sevens_in_a_row([7,2,1,6,2], 1))
	def test_smaller_sevens(self):
		self.assertTrue(not sevens_in_a_row([1,7,1,7,7], 4))

if __name__ == '__main__':
	unittest.main()
