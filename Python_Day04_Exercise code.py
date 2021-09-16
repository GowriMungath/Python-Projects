import random as r
import hai as h

f=r.random()
#gives a floating point value between 0 and 1
print(f)
#gives a floating point value between 0 and 10
print(f*10)

print(h.per)

districts=["Thiruvananthapuram", "Kollam", "Alappuzha", "Pathanamthitta", "Kottayam", "Idukki", "Ernakulam", "Thrissur", "Palakkad", "Malappuram", "Kozhikode", "Wayanadu", "Kannur","Kasaragod"]
print(districts[0])
print(districts[-1])
districts[0]="Trivandram"
print(districts[0])
districts.append("newdistrict")
print(districts)
districts.extend("newdist1","newdist2")
print(districts)

#hai module
import random as r
per=r.randint(1,100)
print(f"Your love has {per}% chance of success.")

import random as r
num=r.randint(0,1)
if num==0:
  print("Heads")
elif num==1:
  print("Tails")

names=input("Enter each person's name seperated by a comma: ")
names=names.split(",")
import random as r
name=names[r.randint(0,len(names)-1)]
#name=r.choice(names)
print(f"Today, {name} should pay the bill")

#placing treasure
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
c=int(position[0])
r=int(position[1])
map[r-1][c-1]='X'
print(f"{row1}\n{row2}\n{row3}")

Family =list(("Achan","Amma","Kannettan","Ponnu","Sreekutty","Dilu"))
print(len(Family))
print(type(Family))
print(Family)

Family1 =list(("Achan","Amma","Kannettan","Ponnu","Sreekutty"))
Family2 =list(("Vappa","Umma","Dilu","Jifree"))
Family=list((Family1,Family2))
print(Family)
