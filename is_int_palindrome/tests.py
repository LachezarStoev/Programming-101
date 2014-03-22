simport unittest
from solution import is_int_palindrome
class PalindromeTest(unittest.TestCase):
	def test_is_palindrome(self):
		self.assertTrue(is_int_palindrome(1))
		self.assertTrue(is_int_palindrome(100001))
		self.assertTrue(is_int_palindrome(999))
	def test_is_not_palindrome(self):
		self.assertTrue(not is_int_palindrome(42))
		self.assertTrue(not is_int_palindrome(123))

if __name__ == '__main__':
	unittest.main()
