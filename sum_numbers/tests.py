import unittest
from subprocess import call
from solution import sum_numbers

class SumNumbersTest(unittest.TestCase):
	def setUp(self):
		self.file_name="sum_numbers_test"
		self.file=open(self.file_name,"w")
	def test_sum_of_five_numbers(self):
		self.file.write("5 10 8 3 7")
		self.file.close()
		self.assertEqual(33,sum_numbers(self.file_name))
	def tearDown(self):
		self.file.close()
		call("rm " + self.file_name,shell=True)

if __name__ == '__main__':
	unittest.main()
