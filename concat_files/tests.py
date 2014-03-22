import unittest
from subprocess import call
from solution import concat_files
class ConcatFilesTest(unittest.TestCase):
	def setUp(self):
		self.file_megatron=open("MEGATRON","r+")
		self.content_megatron=self.file_megatron.read()
		self.file_megatron.close()
		self.file_name="file_with_data_test"
		self.file=open(self.file_name,"w")
		self.file.write("Spam")
		self.file.close()
	def test_one_file_first_concatenate(self):
		self.assertEqual(self.content_megatron + "Spam\n\n",concat_files([self.file_name]))
	def test_two_files_second_concatenate(self):
		self.assertEqual(self.content_megatron + "Spam\n\nSpam\n\n",concat_files([self.file_name,self.file_name]))
	def tearDown(self):
		call("rm " + self.file_name,shell=True)

if __name__ == '__main__':
	unittest.main()



