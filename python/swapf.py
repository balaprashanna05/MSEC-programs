def swap(x,y):
   x=x+y
   y=x-y
   x=x-y
   print("after swapping x="+str(x)+" y="+str(y))
a=int(input("enter first no x="))
b=int(input("enter second no y="))
swap(a,b)
