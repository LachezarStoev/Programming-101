def number_to_list(n):
	digits=[]
	while(n!=0):
		digits.append(n%10)
		n//=10
	digits.reverse()
	return digits
def main():
	print(number_to_list(123))
	print(number_to_list(99999))
	print(number_to_list(123023))

if __name__ == '__main__':
	main()	
