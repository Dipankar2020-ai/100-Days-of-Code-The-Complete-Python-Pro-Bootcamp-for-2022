print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
ans=name1+name2
ans1=ans.lower()
t=ans1.count("t")
r=ans1.count("r")
u=ans1.count("u")
e=ans1.count("e")
true=t+r+u+e
l=ans1.count("l")
o=ans1.count("o")
v=ans1.count("v")
e=ans1.count("e")
love=l+o+v+e
love_score=str(true)+str(love)
love_score1=int(love_score)
if love_score1<10 or love_score1>90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score1>=40 and love_score1<=50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
