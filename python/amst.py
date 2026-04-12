n=int(input("enter a number:"))
x=n
s=0
while(n!=0):
   r=n%10
   s=s+(r*r*r)
   n=n/10
if(x==s):
   print("amstrong number")
else:
   print("not a amstrong number")

   
