programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again.",
  "Loop": "Doing over and over again."
}

print(programming_dictionary["Bug"])

programming_dictionary["Array"]="Homogenous collection of elements stored in contigious locations."
print(programming_dictionary)

emptydict={}

programming_dictionary["Bug"]="A moth in your computer"
print(programming_dictionary["Bug"])
print(programming_dictionary)

for i in programming_dictionary:
  print(i)
  
programming_dictionary={}
print(programming_dictionary)


#students_mark_grading

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades={}

for i in student_scores:
  if student_scores[i]>=91:
    student_grades[i]="Outstanding"
  elif student_scores[i]>=81:
    student_grades[i]="Exceeds Expectations"
  elif student_scores[i]>=71:
    student_grades[i]="Acceptable"
  else:
    student_grades[i]="Fail"
    
print(student_grades)


