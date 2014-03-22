def count_words(arr):
	dict = {}
	for item in arr:
		if item in dict:
			dict[item]+=1
		else:
			dict[item]=1
	return dict