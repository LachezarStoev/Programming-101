import unittest
import re
from subprocess import call
from solution import generate_numbers

class GenerateNumbersTest(unittest.TestCase):
	def test_with_5_numbers(self):
		file_name = "generate_numbers_test"
		count = 5
		generate_numbers(file_name,5)
		test_file=open(file_name,"r")
		content=test_file.read()
		self.assertFalse(not re.search("\d+ \d+ \d+ \d+ \d+",content))
		test_file.close()

if __name__ == '__main__':
	unittest.main()


