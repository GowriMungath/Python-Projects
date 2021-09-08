#average height calculate
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
s=0
count=0
for i in student_heights:
  s=s+i
  count+=1
avg=round(s/count)
print(avg)

