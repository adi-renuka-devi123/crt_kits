# prg7 leap year or not
year=int(input("enter the year:"))
if(year%4==0 & year%100!=0) or (year%400==0):
   print(f"{year} is leap year")
else:
  print(f"{year} is not a leap year")