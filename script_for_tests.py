import os
from subprocess import call

def main():
	dirs=[dir for dir in os.listdir() if dir.find(".") == -1 and dir != "MEGATRON" and dir != "generate_numbers_test"]
	for dir in dirs:
		call("py " + dir + "/tests.py",shell=True)

if __name__ == '__main__':
	main()