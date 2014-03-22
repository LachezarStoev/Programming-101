import unittest
from solution import sum_of_min_and_max
class MinMaxTest(unittest.TestCase):
	def test_range_1_9(self):
		self.assertEqual(10,sum_of_min_and_max([1,2,3,4,5,6,7,8,9]))
	def test_array_with_negative_number(self):
		self.assertEqual(90,sum_of_min_and_max([-10,5,10,100]))
	def test_array_with_one_element(self):
		self.assertEqual(2,sum_of_min_and_max([1]))

if __name__ == '__main__':
	unittest.main()
