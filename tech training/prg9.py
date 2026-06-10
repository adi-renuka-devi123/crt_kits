# prg 9 to read three integer values and find smallest number
a=int(input("enter the first integer: "))
b=int(input("enter the second integer: "))
c=int(input("enter the third integer: "))
if(a<b and a<c):
    print("a is smallest number")
elif(b<c):
    print("b is the smallest number")
else:
    print("c is the smallest number")
