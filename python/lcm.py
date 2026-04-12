a=int(input("enter first no:"))
b=int(input("enter second no:"))
if(a>b):
  x=a
else:
  x=b
while True:
   if(x%a==0 and x%b==0):
     lcm=x
     break
   x=x+1
print("lcm of "+str(a)+" and "+str(b)+" is "+str(lcm))
   
