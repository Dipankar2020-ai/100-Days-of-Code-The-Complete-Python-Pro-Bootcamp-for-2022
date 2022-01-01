import math
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
ans=(weight)/(height*height)
res1=math.ceil(ans)
res=str(math.ceil(ans))
if(res1<18):
    print("Your BMI is "+res+", you are underweight.")
elif(res1>18 and res1<25):
     print("Your BMI is "+res+", you have a normal weight.")
elif(res1>25 and res1<30):
       print("Your BMI is "+res+", you are slightly overweight.")
elif(res1>30 and res1<35):
    print("Your BMI is "+res+",  you are obese.")
else:
    print("Your BMI is "+res+",  you are clinically obese.")
     
