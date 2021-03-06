def contains_digits(number, digits):
	digitsOfNumber=[]
	while number!=0:
		digitsOfNumber.append(number%10)
		number//=10
	for digit in digits:
		if(not digit in digitsOfNumber):
			return False
	return True
	
def main():
	print(contains_digits(402123, [0, 3, 4]))
	print(contains_digits(666, [6,4]))
	print(contains_digits(123456789, [1,2,3,0]))
	print(contains_digits(456, [])) 	
if __name__ == '__main__':
	main()