def val(fraction):
	return fraction[0]/fraction[1]

def sort_fractions(fractions):
	for i in range(1,len(fractions)):
		j=i-1
		temp=fractions[i]
		while(j>=0 and val(fractions[j]) > val(temp)):
			fractions[j+1] = fractions[j]
			j-=1
		fractions[j+1]=temp
	return fractions
