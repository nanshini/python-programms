s=[1,2,4,5,6,7,8,9]
n=len(s)+1
total=0
for i in range(1,n+1):
   total+=i
arr_sum=0
for x in s:
   arr_sum+=x
missing= total - arr_sum
print(missing)
