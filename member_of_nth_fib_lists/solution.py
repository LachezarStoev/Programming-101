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
def member_of_nth_fib_lists(listA,listB,needle):
	n=1
	if listA == [] and listB == []:
		return needle == []
	nth_fib_list=nth_fib_lists(listA,listB,n)
	while len(nth_fib_list) <= len(needle):
		if nth_fib_list == needle:
			return True
		n+=1
		nth_fib_list=nth_fib_lists(listA,listB,n)
	return False

