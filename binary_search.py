def binary_search(arr, k):
	array_len = len(arr)
	L = 0
	R = array_len - 1
	while L <= R:
		M = L + (R-L)//2
		print(f'L={L}, R={R}, M={M}')
		if arr[M] == k:
			return M
		elif arr[M] > k:
			R = M-1
		else:
			L = M+1
	return None
