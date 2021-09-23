logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""
vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""
import time 
flag=1
score=0
while flag==1:
    print(logo)
    print("\n")
    import game_data_day14 as g
    import random as r
    print(f"Your current score = {score}")
    print("\n")
    first=r.choice(g.data)
    sec=r.choice(g.data)
    if first==sec:
        sec=r.choice(g.data)
    print("Compare A: "+first['name']+", "+first['description']+", from "+first['country'])
    print("\n")
    print(vs)
    print("\n")
    print("Against B: "+sec['name']+", "+sec['description']+", from "+sec['country'])
    print("\n")
    ch=input("Guess who has more followers: A or B? ")
    if ch=='A' and first["follower_count"]>sec["follower_count"]:
        print("Yeass you're right!🔥")
        flag=1
        score+=1
    elif ch=='B' and first["follower_count"]<sec["follower_count"]:
        print("Yeass you're right!🔥")
        flag=1
        score+=1
    else:
        print("Oops! Wrong guess. Game Over!😭")
        print(first["name"]+" has "+str(first["follower_count"])+" followers.")
        print(sec["name"]+" has "+str(sec["follower_count"])+" followers.")
        print("\n")
        print(f"Your total score 📢: {score}")
        print("\n")
        flag=0
        exit(0)
    time.sleep(1)
    import os
    os.system("cls")
    
