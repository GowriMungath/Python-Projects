import Guessing_Game_art as G
print(G.art1)
print("I'm thinking of a number between 1 and 100 (Both 1 and 100 Inclusive). I dare you to guess it🤙")
list=[]
for i in range(1,101):
        list.append(i)
import random as r
num=r.choice(list)
level=input('Which level do you prefer? "Easy" or "Hard" ').lower()
def check(a):
        if a-num>0:
                print("Too high!")
        else:
                print("Too low!")
if level=="easy":
        attempts=10
elif level=="hard":
        attempts=5
else:
        print("Invalid Choice!")
print(f"You will get {attempts} attempts to guess!")
a=attempts
flag=0
for i in range(attempts):
        
        inp=int(input("I guess: "))
        if inp<0 or inp>100:
                print("Invalid input")
        elif inp==num:
                print(f"Yayy🤩 That's right🔥 I guessed {num}!")
                flag=1
                exit(0)
        else:
                check(inp)
        print(f"You have {a-(i+1)} attempts remaining")
if not flag==1:
        print(f"I beat ya!😎 I guessed {num}.")
