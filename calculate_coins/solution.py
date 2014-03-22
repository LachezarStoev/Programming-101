def calculate_coins(sum):
	coins={ 1:0, 2:0, 5:0, 10:0, 20:0, 50:0, 100:0 }
	sum=int(sum*100)
	if(sum//100 != 0):
		coins[100]=sum//100
		sum-=sum//100*100
	if(sum//50!=0):
		coins[50]=sum//50
		sum-=sum//50*50
	if(sum//20!=0):
		coins[20]=sum//20
		sum-=sum//20*20
	if(sum//10!=0):
		coins[10]=sum//10
		sum-=sum//10*10
	if(sum//5!=0):
		coins[5]=sum//5
		sum-=sum//5*5
	if(sum//2!=0):
		coins[2]=sum//2
		sum-=sum//2*2
	if(sum//1!=0):
		coins[1]=sum//1
	return coins


def main():
	print(calculate_coins(0.53))
	print(calculate_coins(8.94))

if __name__ == '__main__':
	main()	
