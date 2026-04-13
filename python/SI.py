def fun1(x,y):
   return (x*y*0.12)
def fun2(x,y):
   return(x*y*0.1)
a=int(input("enter profit:"))
b=int(input("enter no of years:"))
c=int(input("If you are sinor citizen then enter 1: "))
if c==1:
   print(fun1(a,b))
else:
   print(fun2(a,b))

