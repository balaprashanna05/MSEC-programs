def fact(n):
   if(n==0):
      return 1
   elif(n>=1):
      return n*fact(n-1)
   else:
      print("enter non negative no")
x=int(input("enter a no "))
ans=fact(x)
print("the factorial of "+str(x)+" is "+str(ans))
