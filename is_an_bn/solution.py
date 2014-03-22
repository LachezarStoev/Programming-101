def is_an_bn(word):
	if len(word) % 2 == 1:
		return False
	for i in range(0,len(word)//2):
		if word[i] != "a" or word[len(word)-i-1] != "b":
			return False
	return True
