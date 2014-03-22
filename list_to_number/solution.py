def list_to_number(digits):
	n=0
	level=1
	for i in range(0,len(digits)):
		n+=digits[len(digits)-i-1]*level
		level*=10
	return n

def main():
	print(list_to_number([1,2,3]))
	print(list_to_number([9,9,9,9,9]))
	print(list_to_number([1,2,3,0,2,3]))

if __name__ == '__main__':
	main()	
