a=input("enter square term:")
b=input("enter coeff term:")
c=input("enter const term:")
d=((b*b)-(4*a*c))
if(d>0):
   ans1=(-b+(d**0.5))/(2*a)
   ans2=(-b-(d**0.5))/(2*a)
   print("the roots are real and distinct:"+str(ans1)+","+str(ans2))
elif(d==0):
   ans3=(-b)/(2*a)
   print("roots are real and equal:"+str(ans3))

else:
   d=-d
   real=(-b)/(2*a)
   img=(d**0.5)/(2*a)
   print("the root are real and img:"+str(real)+"+j"+str(img))



