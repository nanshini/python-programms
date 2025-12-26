s=[1,4,7,2,10,6,8]
first_largest=float("-inf")
second_largest=first_largest
for num in s:
  if num>first_largest:
      second_largest=first_largest
      first_largest=num
  elif num<first_largest and num>second_largest:
       second_largest=num       
print("first_largest:",first_largest)
print("second_largest:",second_largest)
