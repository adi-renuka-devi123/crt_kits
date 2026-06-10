# prg 1 try and exception
"""print("Program starts")
a=10
print("a=",a)
try:
    print(a/0)
except ZeroDivisionError as e:
    print('not possibleto dividbewith zero if you divide it gives',e)
print('program ends')"""

# prg 2 if else exception
"""age=int(input('Enter the age : '))
if(age>=18):
    print("Eligible to vote")
else:
    raise Exception ('Not eligible to vote')"""

# prg 3 withdrawal
"""balance = 5000
try:
    amount = int(input("Enter withdrawl amount: "))
    if amount  > balance:
        raise ValueError("Insufficient Balance")
    print("Withdrawl Successful")
except ValueError as e:
    print("Transactions Failed:",e)
"""
# prg 4 value error
"""try:
    monthly_sal=float(input("enter monthly salary: "))
    if(monthly_sal<=0):
        raise ValueError
    annual_sal=monthly_sal*12
    print("Annual salary: ",annual_sal)
except ValueError:
    print("Please enter a valid salary amt")"""
    
# prg 5 ATM pin
"""pin=input("Enter the password")
try:
    if(pin =='7981'):
        print("login is successful")
    else:
        raise TypeError("incorrect password")
except TypeError as e:
    print(e)"""
    
# prg 6 finally block
a=10
try:
    print(a)
finally:
    print("finally block code")