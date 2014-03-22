def insertionSort(arr):
	for i in range(1,len(arr)):
		j=i-1
		temp=arr[i]
		while j>=0 and arr[j] > temp:
			arr[j+1] = arr[j]
			j-=1
		arr[j+1]=temp

def count_numbers(numbers):
	i = 0
	while i != len(numbers):
		insertionSort(numbers)
		old_len=len(numbers)
		for j in range(i+1,len(numbers)):
			new_number = numbers[j] // numbers[i]
			if not new_number in numbers:
				numbers.append(new_number)
		if len(numbers) > old_len:
			i = 0
		else:
			i += 1
	return len(numbers)




