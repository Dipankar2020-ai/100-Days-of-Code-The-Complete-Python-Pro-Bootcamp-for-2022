import math 
print("Welcome to the tip calculator")
a=float(input("What was the total bill? $"))
b=int(input("What percentage tip would you like to give? 10,12, or 15? "))
c=int(input("How many people to split the bill?"))

tip=(a*b)/100
total=a+tip
res=total/c
final_amount=round(res,2)
print(f"Each person should pay: ${final_amount}")
