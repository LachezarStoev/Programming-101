def magic_string(str):
	changed = 0
	for i in range(0,len(str)//2):
		if str[i] == "<":
			changed+=1
		if str[len(str)-i-1]== ">":
			changed+=1
	return changed
