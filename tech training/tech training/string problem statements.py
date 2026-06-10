# prg 1 department and employee number
"""dept='tech'
empno=123
print(f"{dept.upper()[:3].zfill(3)}-{str(empno).zfill(5)}")"""

#  prg 2 credit card number
"""credit=input("Enter the 16 digit number: ")
print("**** **** ****"+credit[-4:])"""

# prg 3 hdfc bank OTP
"""str='your hdfc bank OTP is 443579 valid for 10 minutes'
print(f"top extracted:{str[22:29]} valid for:{str[39:50]}")
           # (or) 
a=list(map(str,input().split()))
for i in a:
    if i.isdigit():
        print(i)"""
    
# prg 4 valid IFSC code
ifsc=input()
if len(ifsc)==11 and ifsc[:4].isalpha() and ifsc[4] == '0' and ifsc[5:].isalnum():
    print("valid IFSC code")
else:
    print("invalid IFSC code") 