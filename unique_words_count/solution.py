def unique_words_count(arr):
	dict = {}
	for item in arr:
		dict[item]=item
	return len(dict.keys())