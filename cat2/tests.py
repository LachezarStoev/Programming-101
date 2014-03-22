import unittest
from subprocess import call
from solution import cat2

class Cat2Test(unittest.TestCase):
	def setUp(self):
		self.first_file_name="test_file_1"
		self.first_file=open(self.first_file_name,"w")
		self.second_file_name="test_file_2"
		self.second_file=open(self.second_file_name,"w")
		self.third_file_name="test_file_3"
		self.third_file=open(self.third_file_name,"w")
	def test_with_two_files(self):
		self.first_file.write("Python is awesome!")
		self.first_file.close()
		self.second_file.write("You are right, baby!")
		self.second_file.close()
		expected_result="Python is awesome!\n\nYou are right, baby!"
		self.assertEqual(expected_result,cat2([self.first_file_name,self.second_file_name]))
	def test_with_three_files(self):
		self.first_file.write("This")
		self.first_file.close()
		self.second_file.write("That")
		self.second_file.close()
		self.third_file.write("Those")
		self.third_file.close()
		expected_result="This\n\nThat\n\nThose"
		self.assertEqual(expected_result,cat2([self.first_file_name,self.second_file_name,self.third_file_name]))
	def tearDown(self):
		call("rm " + self.first_file_name,shell=True)
		call("rm " + self.second_file_name,shell=True)
		call("rm " + self.third_file_name,shell=True)

if __name__ == '__main__':
	unittest.main()


