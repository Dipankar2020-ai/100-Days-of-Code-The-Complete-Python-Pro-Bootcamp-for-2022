print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
small=15
medium=20
large=25
psmall=2
plarge=3
extra=1
if size=="S":
    res=small
    if add_pepperoni=="Y":
        res=res+psmall
        if extra_cheese=="Y":
            res=res+extra
    else:
         if extra_cheese=="Y":
            res=res+extra


if size=="M":
    res=medium
    if add_pepperoni=="Y":
        res=res+plarge
        if extra_cheese=="Y":
            res=res+extra
    else:
        if extra_cheese=="Y":
            res=res+extra
if size=="L":
    res=large
    if add_pepperoni=="Y":
        res=res+plarge
        if extra_cheese=="Y":
            res=res+extra
        else:
            if extra_cheese=="Y":
                res=res+extra
print(f"Your final bill is: ${res}.")
