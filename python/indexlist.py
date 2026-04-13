a=[1,9,4,5,9]
print(a)
d=0
for i in range (len(a)):
    print("index of",a[i],"is",i)
    b=a.count(a[i])
    c=a[i]
    if b> 1 and c!=d:
       d=a[i]
       print("The element",a[i]," is repeated ",b,"times")
   
     
      

      
