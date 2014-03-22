import sys
from random import randint

def generate_numbers(file_name,count):
	my_file=open(file_name,"w")
	while count > 0:
		if count != 1:
			my_file.write(str(randint(1, 1000)) + " ")
		else:
			my_file.write(str(randint(1, 1000)))
		count -= 1
	my_file.close()

def main():
	generate_numbers(sys.argv[1],sys.argv[2])

if __name__ == '__main__':
	main()
