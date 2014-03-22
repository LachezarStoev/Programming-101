from math import sqrt
def is_prime(n):
	if n<2:
		return False
	for i in range(2,int(sqrt(n))+1):
		if n%i == 0:
			return False
	return True
def main():
	print(is_prime(1))
	print(is_prime(2))
	print(is_prime(8))
	print(is_prime(11))
	print(is_prime(-10))
if __name__ == '__main__':
	main()