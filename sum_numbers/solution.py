import sys
def sum_numbers(filename):
	my_file=open(filename,"r")
	content=my_file.read()
	my_file.close()
	content=content.split(" ")
	return sum([int(n) for n in content])
def main():
	print(sum_numbers(sys.argv[1]))

if __name__ == '__main__':
	main()
