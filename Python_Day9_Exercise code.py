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
