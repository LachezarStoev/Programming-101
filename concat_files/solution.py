import sys
def concat_files(filenames):
	file_megatron=open("MEGATRON","a+")
	for filename in filenames:
		my_file=open(filename,"r")
		content=my_file.read()
		my_file.close()
		file_megatron.write(content+"\n\n")
	file_megatron.close()
	file_megatron=open("MEGATRON","r")
	content=file_megatron.read()
	file_megatron.close()
	return content

def main():
	concat_files(sys.argv[1:])
	
if __name__ == '__main__':
	main()