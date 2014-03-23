import unittest
from solution import PizzaDelivery
from subprocess import call
class PizzaDeliveryTest(unittest.TestCase):
	def setUp(self):
		self.pizza=PizzaDelivery()
	def test_take_and_status(self):
		self.pizza.take("Rado",10)
		self.assertEqual("Rado - 10",self.pizza.status())
		self.pizza.take("Rado",20)
		self.assertEqual("Rado - 30",self.pizza.status())
		self.pizza.take("RadoRado",25)
		expected = "Rado - 30\nRadoRado - 25"
		#self.assertEqual(expected,self.pizza.status())
		#dictionary is fast and we don't want sorted status
		#this is the reason of our unexpected result
	def test_init_orders(self):
		file=open("orders/test_file","w")
		file.close()
		test_pizza=PizzaDelivery()
		self.assertEqual("[1] - test_file",test_pizza.list())		

	def test_list(self):
		self.pizza.take("Rado",30)
		first_date=self.pizza.save()
		self.pizza.take("Rado",30)
		second_date=self.pizza.save()
		expected="[1] - " + first_date + "\n" + "[2] - " + second_date
		self.assertEqual(expected,self.pizza.list())

	def test_save(self):
		self.pizza.take("Lucho" , 30)
		self.pizza.take("Rado" , 20)
		expected = self.pizza.status()
		current_date = self.pizza.save()
		test_file=open("orders/" + current_date,"r")
		file_content=test_file.read()
		test_file.close()
		self.assertEqual(expected,file_content)
	def test_load(self):
		file=open("orders/order-2013","w")
		file.write("Rado - 30")
		file.close()
		file=open("orders/order-2014","w")
		file.write("Bai Ivan - 5")
		file.close()
		test_pizza=PizzaDelivery()
		test_pizza.load(2)
		expected = "Bai Ivan - 5"
		self.assertEqual(expected,test_pizza.status())
		test_pizza.load(1)
		expected_again="Rado - 30"
		self.assertEqual(expected_again,test_pizza.status())
	def tearDown(self):
		call("rm -rf orders",shell=True)




if __name__ == '__main__':
	unittest.main()
