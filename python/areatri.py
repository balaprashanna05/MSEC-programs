import math
print("enter the choice 2 for two inputs and 3 for three inputs")
x=int(input())
if(x==2):
   h=input("enter height:")
   b=input("enter breadth:")
   if(h>0 and b>0):
    a=0.5*h*b
    print("area of triangle:"+str(a))
   else:
      print("enter +ve no")
elif(x==3):
   a=float(input("enter side1:"))
   b=float(input("enter side2:"))
   c=float(input("enter side3:"))
   s=(a+b+c)/2
   if(a>0 and b>0 and c>0):
      area=math.sqrt(s*(s-a)*(s-b)*(s-c))
      print("area of triangle:"+str(area))
   else:
      print("enter +ve no")
else:
   print("invalid choice")

