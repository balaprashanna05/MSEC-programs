print("enter 1 to calculate simple interest or enter two to calculate compound interest")
x=int(input())
p=float(input("enter principle amt:"))
n=float(input("enter no of years:"))
r=float(input("enter rate of interest:"))
if(x==1):
   si=(p*n*r)/100
   print("simple interest:"+str(si))
elif(x==2):
   t=float(input("enter time period:"))
   ci=((((r/(n*100))+1)**(n*t))*p)-p
   print("compound interest:"+str(ci))
else:
   print("invalid choice")

