number = int(input("Which number do you want to check? "))
if number%2==0:
  print("This is an even number.")
else:
  print("This is an odd number.")

#roller_coaster
height=float(input("Enter your height in Cms: "))
if height>120:
    print("welcome to the roller coaster ride!")
    age=int(input("Enter your age: "))
    if age<12:
        print("Please pay $5.")
    elif age<=18:
        print("Please pay $7")
    else:
        print("Please pay $12")
else:
    print("Entry denied!")

#BMI_Calculator_2.0
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi=round(weight/(height**2),2)
if bmi<18.5:
  print(f"Your BMI is {bmi} and you are underweight")
elif bmi<25:
  print(f"Your BMI is {bmi} and you have a normal weight")
elif bmi<30:
  print(f"Your BMI is {bmi} and you are slightly overweight")
elif bmi<35:
  print(f"Your BMI is {bmi} and you are obese")
else:
  print(f"Your BMI is {bmi} and you are clinically obese")

#Leap_year_checker
year = int(input("Which year do you want to check? "))
if year%400==0:
  print("Leap Year")
elif year%4==0:
  if year%100==0:
    print("Not a leap year")
  else:
    print("Leap Year")
else:
  print("Not a leap year")

#Roller coaster again
height=float(input("Enter your height in Cms: "))
if height>120:
    print("welcome to the roller coaster ride!")
    age=int(input("Enter your age: "))
    if age<12:
        bill=5
    elif age<=18:
        bill=7
    else:
        bill=12
    ans=input("Do you want picture ? Y or N ")
    if ans=="Y":
        bill+=3
    print(f"Please pay {bill}.")
else:
    print("Entry denied!")

#Pizza order
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
if size=="S":
  bill=15
  if add_pepperoni=="Y":
    bill+=2
elif size=="M":
  bill=20
  if add_pepperoni=="Y":
    bill+=3
elif size=="L":
  bill=25
  if add_pepperoni=="Y":
    bill+=3

if extra_cheese=="Y":
  bill+=1

print(f"Your final bill is: {bill}.")

#Love Calculator
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
name=name1+name2
count1=0
a=len(name)
for i in range(a):
  if name[i]=="T"or name[i]=="R" or name[i]=="U" or name[i]=="E"or name[i]=="t"or name[i]=="r" or name[i]=="u" or name[i]=="e":
    count1+=1

count2=0
a=len(name)
for i in range(a):
  if name[i]=="L"or name[i]=="O" or name[i]=="V" or name[i]=="E" or name[i]=="l"or name[i]=="o" or name[i]=="v" or name[i]=="e":
    count2+=1

final=str(count1)+str(count2)
if int(final)<10 or int(final)>90:
  print(f"Your score is {final}, you go together like coke and mentos.")
elif int(final)>40 and int(final)<50:
  print(f"Your score is {final}, you are alright together.")
else:
  print(f"Your score is {final}.")




