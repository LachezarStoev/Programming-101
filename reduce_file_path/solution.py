import re
def reduce_file_path(path):
	new_path= re.sub("/$","",path)
	new_path=re.sub("/+","/",new_path)
	new_path=re.sub("(/\w*(/\.)+)?/?\w*/\.\.","",new_path)
	new_path=re.sub("/\.","",new_path)
	if new_path == "":
		return "/"
	return new_path


