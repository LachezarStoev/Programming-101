def prepare_meal(number):
	n=1
	n_times_spam=0
	while 3**n <= number :
		if number % 3**n == 0:
			n_times_spam=n
		n+=1
	if number % 5 == 0:
		if n_times_spam != 0:
			return "spam " * n_times_spam + "and eggs"
		else:
			return "eggs"
	else:
		return ("spam " * n_times_spam).strip()
