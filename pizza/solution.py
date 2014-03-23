from time import time
from datetime import datetime
from glob import glob
from subprocess import call
import os

class PizzaDelivery():
	def __init__(self):
		self.__names_of_orders={}
		self.__current_order={}
		self.__count=0
		self.initiliaze_orders()

	def initiliaze_orders(self):
		if glob("orders") == []:
			call("mkdir orders",shell=True)
		else:
			orders_names = os.listdir("orders")
			for order_name in orders_names:
				self.__names_of_orders[self.__count+1]=order_name
				self.__count+=1
	def list(self):
		result = []
		for key in range(1,self.__count+1):
			result.append("[{}] - {}".format(key,self.__names_of_orders[key]))
		return "\n".join(result)

	def take(self,name,price):
		if name in self.__current_order:
			self.__current_order[name]+=price
		else:
			self.__current_order[name]=price
	def status(self):
		current_status = []
		for key in self.__current_order:
			current_status.append("{} - {}".format(key,self.__current_order[key]))
		return "\n".join(current_status)	
	def save(self):
		ts = time()
		stamp = datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')
		file=open("orders/" + stamp,"w")
		file.write(self.status())
		file.close()
		self.__current_order = {}
		self.__names_of_orders[self.__count+1]=stamp
		self.__count+=1
		return stamp
	def load(self,order_index):
		self.__current_order={}
		file=open("orders/" + self.__names_of_orders[order_index],"r")
		content=file.read()
		file.close()
		content=content.split("\n")
		for line in content:
			pair=line.split(" - ")
			self.__current_order[pair[0]]=pair[1]

def main():
	pizza=PizzaDelivery()
	while(True):
		com = input("Enter command>")
		com=com.split(" ")
		if com[0] == "take":
			pizza.take(com[1],com[2])
		elif com[0] == "status":
			print(pizza.status())
		elif com[0] == "save":
			pizza.save()
		elif com[0] == "list":
			print(pizza.list())
		elif com[0] == "load":
			pizza.load(int(com[1]))
		elif com[0] == "finish":
			break
		else:
			print("Unknown command!")
	#this is so clear! :D made for you, not client
 
if __name__ == '__main__':
	main()
















