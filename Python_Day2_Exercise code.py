#datatypes
print("Gowri"[0])
print("Gowri"[3])
print("1425"[2])
print("123"+"456")
print(123+456)
print(123_456_789)
print(3.134)
print(True)
print(False)

city=input("Which is your favourite city? ")
val=len(city)
print(type(val))
value_in_string=str(val)
print(type(value_in_string))
print("Your favourite city has "+value_in_string+" characters")

a=123
print(type(a))
print(type(str(a)))
print(type(float(a)))
print(70+float("100.5"))
print(str(70)+str(100))

#add digits of a 2 digit number
num=int(input("Enter a number"))
a=num%10
num=num-a
b=num/10
print(a+b)

OR

#add digits of a 2 digit number
num=(input("Enter a number"))
a=int(num[1])
b=int(num[0])
print(a+b)
