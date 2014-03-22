def is_int_palindrome(n):
	digits=[]
	while(n!=0):
		digits.append(n%10)
		n//=10
	for i in range(0,len(digits)):
		if(digits[i]!=digits[len(digits)-i-1]):
			return False
	return True
def main():
	print(is_int_palindrome(1))
	print(is_int_palindrome(42))
	print(is_int_palindrome(100001))
	print(is_int_palindrome(999)) 	
	print(is_int_palindrome(123))
if __name__ == '__main__':
	main()