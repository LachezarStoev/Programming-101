import unittest
from subprocess import call
from solution import wc
class WCTest(unittest.TestCase):
	def setUp(self):
		self.file_name="count_chars_words_lines"
		self.file=open(self.file_name,"w")
		self.file.write("Here is the moment\nIs here?")
		self.file.close()
	def test_words(self):
		self.assertEqual(6,wc("words",self.file_name))
	def test_lines(self):	
		self.assertEqual(2,wc("lines",self.file_name))
	def test_chars(self):
		self.assertEqual(27,wc("chars",self.file_name))
	def tearDown(self):
		call("rm " + self.file_name,shell=True)

if __name__ == '__main__':
	unittest.main()
