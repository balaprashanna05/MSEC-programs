x=str(input("enter temperature:"))
y=str(input("enter humidity:"))
if(x=="warm"):
   if(y=="humid"):
      print("play tennis")
   elif(y=="dry"):
      print("play basketball")
   else:
      print("invalid humidity...")
elif(x=="cold"):
   if(y=="humid"):
      print("swimmimg")
   elif(y=="dry"):
     print("play cricket")
   else:
     print("invalid humidity...")
else:
   print("invalid temperature")

