def optimized_bubble_sort(arr):
	arr_len = len(arr)
	iteration_count = 0
	for i in range(arr_len):
		swapped = False
		for j in range(arr_len-i-1):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
				swapped = True
		iteration_count += 1

		if not swapped:
			break
	
	print("Sorted array", arr)
	print("Iteration count", iteration_count)
