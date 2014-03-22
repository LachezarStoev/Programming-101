def wc(comm,filename):
	my_file=open(filename,"r")
	content=my_file.read()
	my_file.close()
	if comm == "lines":
		return len(content.splitlines())
	elif comm == "words":
		content = content.replace("\n"," ")
		return len(content.split(" "))
	elif comm == "chars":
		content.replace("\n"," ")
		return len(content)
	else:
		print("Invalid command.Try again.\n")
