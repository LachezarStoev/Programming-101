def what_is_my_sign(day, month):
	if month == 3 and day in range(21,32) or month==4 and day in range(1,21) :
		return "Aries"
	elif month == 4 and day in range(21,31) or month==5 and day in range(1,22):
		return "Taurus"
	elif month == 5 and day in range(22,32) or month==6 and day in range(1,22):
		return "Gemini"
	elif month == 6 and day in range(22,31) or month==7 and day in range(1,23):
		return "Cancer"
	elif month == 7 and day in range(23,32) or month==8 and day in range(1,23):
		return "Leo"
	elif month == 8 and day in range(23,32) or month==9 and day in range(1,24):
		return "Virgo"
	elif month == 9 and day in range(24,31) or month==10 and day in range(1,24):
		return "Libra"
	elif month ==10 and day in range(24,32) or month==11 and day in range(1,23):
		return "Scorpio"
	elif month ==11 and day in range(23,31) or month==12 and day in range(1,22):
		return "Sagittarius"
	elif month ==12 and day in range(22,32) or month==1 and day in range(1,21):
		return "Capricorn"
	elif month == 1 and day in range(21,32) or month==2 and day in range(1,20):
		return "Aquarius"
	elif month == 2 and day in range(20,30) or month==3 and day in range(1,21):
		return "Pisces"
	else:
		return "Invalid input.\n"
def main():
	print(what_is_my_sign(5, 8))
	print(what_is_my_sign(29, 1))
	print(what_is_my_sign(30, 6))
	print(what_is_my_sign(31, 5))
	print(what_is_my_sign(2, 2))
	print(what_is_my_sign(8, 5))
	print(what_is_my_sign(9, 1))

if __name__ == '__main__':
	main()	
