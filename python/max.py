def max(x,y,z):
   if(x>y and x>z):
      print("the largest no is "+str(x))
   elif(y>x and y>z):
      print("the largest no is "+str(y))
   else:
      print("the largest no is "+str(z))
a=int(input("enter first no:"))
b=int(input("enter second no:"))
c=int(input("enter third no:"))
max(a,b,c)
