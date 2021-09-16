def name(f_name,l_name):
    return f_name+" "+l_name


f=input("Enter your first name: ").title()
l=input("Enter your last name: ").title()
print(f"Your name is: {name(f,l)}")

#number of days in a month
def is_leap(year):
  if (year%400==0) or (year%4==0 and year%100!=0):
    return True
  else:
    return False

def days_in_month(year,month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if month<1 or month>12:
    return "invalid input"
  elif(month==2):
    res=is_leap(year)
    if res==True:
      return 29
    else:
      return 28
  else:
    return month_days[month-1]
  
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)


