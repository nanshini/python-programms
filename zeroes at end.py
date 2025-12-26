s=[1,10,10,2,4,0,7,8,0,0,11,12]
res=[]
for num in s:
  if num!=0:
    res.append(num)
print(res+[0]*(len(s)-len(res)))
