def selection_sort(arr):
	array_len = len(arr)
	for i in range(array_len):
		min = i	
		for j in range(i, array_len):
			if arr[j] < arr[min]:
				min = j
		arr[min], arr[i] = arr[i], arr[min]
	print("Sorted list is", arr)
