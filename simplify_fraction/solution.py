def gcd(x,y):
	if y==0:
		return x
	else:
		return gcd(y, x%y)
def simplify_fraction(fraction):
	maxDiv=gcd(fraction[1],fraction[0])
	return (fraction[0]//maxDiv,fraction[1]//maxDiv)
