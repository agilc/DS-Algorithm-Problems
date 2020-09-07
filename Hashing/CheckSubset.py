def is_subset(arr1,arr2):
  hash_set = set()
  for item in arr1:
    hash_set.add(item)

  for item in arr2:
    if item not in hash_set:
      print("Not a subset")
      return
  print("A valid subset")