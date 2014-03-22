def is_number_balanced(n):
	digits=[]
	while(n!=0):
		digits.append(n%10)
		n//=10
	leftPart=0
	rightPart=0
	for i in range(0,len(digits)//2):
		leftPart+=digits[i]
		rightPart+=digits[len(digits)-i-1]
	if(leftPart==rightPart):
		return True
	return False
		
def main():
	print(is_number_balanced(9))
	print(is_number_balanced(11))
	print(is_number_balanced(13))
	print(is_number_balanced(121))
	print(is_number_balanced(4518))
	print(is_number_balanced(28471))
	print(is_number_balanced(1238033))

if __name__ == '__main__':
	main()