import unittest
from solution import reduce_file_path
class FilePathTest(unittest.TestCase):
	def test_simple_path(self):
		self.assertEqual("/", reduce_file_path("/"))
		self.assertEqual("/srv/www/htdocs/wtf",reduce_file_path("/srv/www/htdocs/wtf/"))
		self.assertEqual("/srv/www/htdocs/wtf", reduce_file_path("/srv/www/htdocs/wtf"))
	def test_with__more_slashes(self):
		self.assertEqual("/",reduce_file_path("//////////////"))
		self.assertEqual("/etc/wtf",reduce_file_path("/etc//wtf/"))
	def test_with_one_dot(self):
		self.assertEqual("/srv",reduce_file_path("/srv/./././././"))
		self.assertEqual("/home",reduce_file_path("/home/./"))
	def test_with_two_dots(self):
		self.assertEqual("/",reduce_file_path("/srv/../"))
		self.assertEqual("/",reduce_file_path("/etc/../etc/../etc/../"))
		self.assertEqual("/",reduce_file_path("/../"))
		self.assertEqual("/",reduce_file_path("/etc/.."))
		self.assertEqual("/",reduce_file_path("/etc/../"))
		self.assertEqual("/etc/code",reduce_file_path("/etc/home/../code"))
		self.assertEqual("/",reduce_file_path("/.."))
		self.assertEqual("/home",reduce_file_path("/home//../////home"))
		self.assertEqual("/home/home",reduce_file_path("/../////home/home/././../home/"))
		self.assertEqual("/",reduce_file_path("/home/././../"))
		self.assertEqual("/lacho",reduce_file_path("/home/././../lacho"))
		self.assertEqual("/",reduce_file_path("/home/../././"))


if __name__ == '__main__':
	unittest.main()
