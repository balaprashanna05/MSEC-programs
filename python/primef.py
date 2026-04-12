def prime(n):
   if(n==2):
      return 1
   else:
      for i in range(2,n):
	 if(n%i==0):
	    flag=1
	    break
	 flag=0  
      if(flag==0):
	 return 1
      else:
	 return 0
x=int(input("enter a number "))
ans=prime(x)
if(ans==1):
   print("prime no")
else:
   print("not a prime no")
