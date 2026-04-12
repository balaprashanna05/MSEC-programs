

input_str=input("Enter two strings separated by a space: ")
str1,str2=input_str.split()
nstr1=str2[0:2] + str1[2:]
nstr2=str1[0:2] + str2[2:]
ans=nstr1+ " " +nstr2
print(ans)

