import sys
def cat(file_name):
	my_file=open(file_name,"r")
	content=my_file.read()
	my_file.close()
	return content

def main():
	print(cat(sys.argv[1]))	

if __name__ == '__main__':
	main()

