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

print(5+6)
print(6-3)
print(3*4)
print(7/3)
print(int(7/3))
print(7//3)
print(type(6/3))
print(2**3)
print(3*3+3/3-3)
print(3*(3+3)/3-3)
print(8/3)
print(round(8/3))
print(round(8/3, 3))
a=5
print(a)
a/=2
print(a)
height=150.9
weight=37.8
s=True
print(f"I weigh {weight} and is {height} tall. Yes it's {s}!")
