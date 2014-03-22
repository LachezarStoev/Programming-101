def nth_fib_lists(listA,listB,n):
	if n==1:
		return listA
	if n==2:
		return listB
	listC = listA + listB
	for i in range(3,n+1):
		listA=listB
		listB=listC
		listC=listA+listB
	return listB
	
		