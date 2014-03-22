from math import sqrt
def is_prime(n):
	if n<2:
		return False
	for i in range(2,int(sqrt(n))+1):
		if n%i == 0:
			return False
	return True

def goldbach(n):
	i=2
	list_of_tuples=[]
	while 2*i <= n:
		if is_prime(i) and is_prime(n-i):
			list_of_tuples.append((i,n-i))
		i+=1
	return list_of_tuples