def final_position(commands,min,max):
	pos = 0
	for com in commands:
		if com == "R":
			if pos < max:
				pos+=1
		else:
			if -min < pos:
				pos-=1
	return pos


