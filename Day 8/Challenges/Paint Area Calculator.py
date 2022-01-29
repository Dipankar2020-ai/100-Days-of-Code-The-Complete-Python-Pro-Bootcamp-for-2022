import math
def paint_calc(height,width,coverage):
    numberofcans=(height*width)/coverage
    print(f"You'll need {math.ceil(numberofcans)} cans of paint")





#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage1= 5
paint_calc(height=test_h, width=test_w, coverage=coverage1)
