import unittest
from solution import cat
from subprocess import call
class CatTest(unittest.TestCase):
	def setUp(self):
		self.name="test_cat_command"
		self.file=open(self.name,"w")
	def test_cat_command(self):
		self.file.write("Test some text")
		self.file.close()
		self.assertEqual("Test some text",cat(self.name))
	def tearDown(self):
		call("rm " + self.name,shell=True)

if __name__ == '__main__':
	unittest.main()
