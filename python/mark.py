def tot(v,w,x,y,z):
     return (x+y+z+v+w)
def avg(v,w,x,y,z):
     return (x+y+z+v+w)/5
a=int(input("enter 1st mark: "))
b=int(input("enter 2nd mark: "))
c=int(input("enter 3rd mark: "))
d=int(input("enter 4th mark: "))
e=int(input("enter 5th mark: "))
print("total=",tot(a,b,c,d,e))
print("average=",avg(a,b,c,d,e))
