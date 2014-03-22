def groupby(func, seq):
	dict = {}
	for item in seq:
		if func(item) in dict:
			dict[func(item)].append(item)
		else:
			dict[func(item)]=[]
			dict[func(item)].append(item)
	return dict