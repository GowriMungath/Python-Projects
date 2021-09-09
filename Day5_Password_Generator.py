#without using shuffle()
print("Welcome to PyPassword Generator!")

numbers=[0,1,2,3,4,5,6,7,8,9]

symbols=['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']

import string
letters=list(string.ascii_lowercase)
upletters=list(string.ascii_uppercase)
letters.append(upletters)

list = [numbers,symbols,letters]

num_letters=int(input("How many letters would you like in your password? "))
num_symbols=int(input("How many symbols would you like? "))
num_numbers=int(input("How many numbers would you like? "))


import random as r
p=" "
countnum=0
countsym=0
countlet=0
flag=0
while flag==0:
    this=r.choice(list)
    if this==list[0]:
        countnum+=1
        if countnum<=num_numbers:
            password=str(r.choice(this))
            p=p+password
    elif this==list[1]:
        countsym+=1
        if countsym<=num_symbols:
            password=r.choice(this)
            p=p+password
    else:
        countlet+=1
        if countlet<=num_letters:
            password=r.choice(this)
            p=p+password
    if len(p)==num_letters+num_symbols+num_numbers:
        break
    

print(f"Here is your password: {p}")

OR

#using shuffle()
print("Welcome to PyPassword Generator!")

numbers=[0,1,2,3,4,5,6,7,8,9]

symbols=['~', ':', "'", '+', '[', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']

import string
letters=list(string.ascii_lowercase)
upletters=list(string.ascii_uppercase)
letters.append(upletters)

list = [numbers,symbols,letters]

num_letters=int(input("How many letters would you like in your password? "))
num_symbols=int(input("How many symbols would you like? "))
num_numbers=int(input("How many numbers would you like? "))


import random as r
password=[]
for i in range(0,num_letters):
    l=r.choice(letters)
    password.append(l)
for i in range(0,num_numbers):
    n=str(r.choice(numbers))
    password.append(n)
for i in range(0,num_symbols):
    s=r.choice(symbols)
    password.append(s)
sum=num_letters+num_numbers+num_symbols
r.shuffle(password)
for i in password:
    print(i, end="")

