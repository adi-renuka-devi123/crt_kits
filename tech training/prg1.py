age=int(input("Enter your age:"))
if(age>=18):
    print("eligible to vote")
else:
    print("not eligible to vote")
    
    # using ternary operator:
res="eligible"if age>=18 else "not eliglble"
print("you are",res,"to vote")
