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

