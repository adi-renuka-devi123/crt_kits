# prg 8 to read three integer values and find largest number
a=int(input("enter the first integer: "))
b=int(input("enter the second integer: "))
c=int(input("enter the third integer: "))
if(a>b and a>c):
    print("a is largest number")
elif(b>c):
    print("b is the largest number")
else:
    print("c is the largest number")
