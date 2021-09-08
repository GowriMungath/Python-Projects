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

#high score calculate
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
high=student_scores[0]
for i in student_scores:
  if i>high:
    high=i
print(f"The highest score in the class is: {high}")



