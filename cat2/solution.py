import sys
def cat2(filenames):
	all_content=[]
	for filename in filenames:
		my_file=open(filename,"r")
		all_content.append(my_file.read())
		my_file.close()
	return "\n\n".join(all_content)
def main():
	print(cat2(sys.argv[1:]))
if __name__ == '__main__':
	main()
