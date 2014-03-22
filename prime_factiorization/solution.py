from itertools import dropwhile, takewhile
def prime_factorization(n):
	divs=[]
	while(n>1):
		for div in range(2,n+1):
			if(n%div==0):
				divs.append(div)
				n//=div
				break
	result=[]
	while(divs != []):
		countOfDiv=list(takewhile(lambda x: x==divs[0], divs))
		result.append((countOfDiv[0],len(countOfDiv)))
		divs=list(dropwhile(lambda x: x==divs[0],divs))
	return result
def main():
	print(prime_factorization(10))
	print(prime_factorization(14))
	print(prime_factorization(356))
	print(prime_factorization(89))
	print(prime_factorization(1000))

if __name__ == '__main__':
	main()	
