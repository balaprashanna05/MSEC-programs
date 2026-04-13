a=int(input("enter the hour timing of entry "))
b=int (input("enter the minute timing of entry "))
c=int(input("enter the hour timing of leaving "))
d=int(input("enter the minute timing of leaving "))
x=c-a
y=d-b
z=(x*60)+y
hour=z//60
mint=z%60
print("the total hours the vehicle stayed is",hour,":",mint)
if z>180 :
   print("the parking ost for")
   print("truck or bus = rs 30")
   print("car = rs 20")
   print("cycle or bike = rs 10")
else:
   print("the parking cost for")
   print("truck or bus = rs 20")
   print("car = rs 10")
   print("cycle or bike = rs 5")


