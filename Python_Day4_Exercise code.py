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
