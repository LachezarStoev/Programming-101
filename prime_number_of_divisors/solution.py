from math import sqrt

def number_of_divisors(n):
	count=0
	for div in range(1,n+1):
		if n%div==0:
			count+=1
	return count

def is_prime(n):
	if n<2:
		return False
	for i in range(2,int(sqrt(n))+1):
		if n%i == 0:
			return False
	return True

def prime_number_of_divisors(n):
	if(is_prime(number_of_divisors(n))):
		return True
	return False

def main():
	print(prime_number_of_divisors(7))
	print(prime_number_of_divisors(8))
	print(prime_number_of_divisors(9))
if __name__ == '__main__':
	main()