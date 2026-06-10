# prg 1 sales revenue daily tracker
"""n=7
revenue=[]
for i in range(n):
    ele=int(input(f"enter the revenue for day {i+1}:"))
    revenue.append(ele)
print(f"total revenue: {sum(revenue)} | best day: {max(revenue)} | worst day: {min(revenue)}")

                # (or)
revenue=list(map(int,input("enter the revenue for 7 days:").split()))
print(f"total revenue: {sum(revenue)} | best day: {max(revenue)} | worst day: {min(revenue)}")"""

# prg 2 employee onboarding
"""candidates = ["Amit", "Priya", "Rahul"]
print(" Initial list:", candidates)
candidates.append("Sneha")
print("After adding from last:", candidates)
removed1 = candidates.pop(0)
print(" Removed from first:", removed1, "List:", candidates)
candidates.insert(0, "Ananya")
print(" After adding at highest priority:", candidates)
print("\nFinal list:", candidates)"""

# prg 3 ecommerce
"""price=list(map(int,input("enter the prices:").split()))
new_list=[]
for i in price:
    if i in price:
        new_list.append(i)
print(new_list)

                 #(or)
price=list(map(int,input("enter the prices:").split()))
print([i for i in price if i>1000])"""

# prg 4 attendence
"""atd=list(map(str,input("enter the atd:").lower().split()))
print(f"no.of absents are {atd.count("absent")}")"""

# prg 5 top scorer in platform
"""sco=list(map(int,input("enter scores").split()))
print(f"ranked: {sorted(sco,reverse=True)} | top scorer: {max(sco)}")"""

# prg 6 server loger error extract
"""codes=list(map(int,input("enter the http codes:").split()))
last_five=codes[-5:]
print(f"last five records:{last_five} | critical error found:{True if 500 in last_five else False}")"""

# prg 7 warehouse management system
"""g1=list(map(int,input("enter the godown a:").split()))
g2=list(map(int,input("enter the godown b:").split()))
print('unified inventory:{set(g1+g2)} | total tength:{len(g1+g2)}')"""

# prg 8 average nps score
"""score=list(map(int,input("enter the nps score").split()))
avg=sum(score)/len(score)
print(f'average nps score{avg:.2f}')"""

# prg 9 meeting room availability check slot
"""slot=list(map(str,input("Enter the booked slot:").split()))
time_slot=list(input("Enter the requested slot:"))
print("slot already booked"if time_slot in slot else "slot is available")"""

# prg 10 product selling units
"""prod=list(map(int,input("enter rates:").split()))
print(f"top 3: {sorted(prod,reverse=True)[:3]} ")"""

# prg 11 weekly expences generator
"""expences=list(map(int,input("enter expences for 7 days:").split()))
print(f"day 1:{expences[0]} | day 2:{expences[1]} | day 3:{expences[2]} | day 4:{expences[3]} | day 5:{expences[4]} | day 6:{expences[5]} | day 7:{expences[6]} ")"""

# prg 12 