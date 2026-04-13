a=[1,4,6,7,8,8,8,9,1]
print(a)
for i in range (len(a)):
   if (a.count(a[i])) > 1:  
     print(a[i])
     

