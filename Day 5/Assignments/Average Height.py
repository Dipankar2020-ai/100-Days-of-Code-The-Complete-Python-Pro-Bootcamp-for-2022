import math
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
sum1=0
count=0
for i in student_heights:
    sum1=sum1+i
    count=count+1
ans=sum1/count
print(round(ans))
