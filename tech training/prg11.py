# prg 11 to read three integer values and find the middle number
a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))
c = int(input("Enter the third integer: "))

if (b < a and a < c) or (c < a and a < b):
    print(f"The middle number is: {a}")
elif (a < b and b < c) or (c < b and b < a):
    print(f"The middle number is: {b}")
else:
    print(f"The middle number is: {c}")