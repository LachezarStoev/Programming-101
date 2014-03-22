def sum_of_divisors(n):
	sum=0
	for div in range(1,n+1):
		if(n%div==0):
			sum+=div
	return sum

def main():
    print(sum_of_divisors(8))
    print(sum_of_divisors(7))
    print(sum_of_divisors(1))
    print(sum_of_divisors(1000))

if __name__ == '__main__':
    main()