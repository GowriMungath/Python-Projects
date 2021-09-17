def print_logo():
    logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
    print(logo)

def ace_case(lis):
    ch=r.choice(lis)
    lis.append(ch)
    if 11 in lis and sum(lis)>21:
        lis.remove(11)
        lis.append(1)
    return lis

def draw(comp,user):
    if sum(comp)==sum(user):
        print("Draw 🙃")  
        return 1

def computer(comp,user):
    if len(comp) == 2:
        if sum(comp)==21:
            print("Lose, opponent has Blackjack 😱")
            return 
    while sum(comp)<=17:
        if sum(comp)<21:
            comp=ace_case(comp)
    print(f"Computer's final hand: {comp} score: {sum(comp)}")  
    ret=draw(comp,user)
    if not ret==1:
        if sum(comp)>21:
            print("Opponent went over. You win 😁")
            return
        elif sum(comp)>sum(user):
            print("You lose")
            return
        else:
            print("You win 😁")
            return

def use(user):
    if sum(user)==21:
        print("You win 😁")
        return
    else:
        c=input("Type 'y' to get another card, type 'n' to pass: ")
        while c=='y':
            user=ace_case(user)
            print(f"Your cards: {user} Your score: {sum(user)}")
            if sum(user)>21:
                print("You went over. You lose 😤")
                return 1
            elif sum(user)==21:
                print("You win 😁")
                return 1
            c=input("Type 'y' to get another card, type 'n' to pass: ")
        print(f"Your final hand: {user} Your score: {sum(user)}")
        if not c=='y'and not c=='n':
            print("Invalid choice!")
            exit(0)

def main():
    user=[]
    comp=[]
    for i in range(2):
        ch=r.choice(list)
        user.append(ch)
    print(f"Your cards: {user} Your score: {sum(user)}")
    if sum(user)==21:
        print("Win with a Blackjack 😎")
        return
    else:
        ch2=r.choice(list)
        comp.append(ch2)
        print(f"Computer's first card: {comp[0]}")
        ret=use(user)
        if ret==1:
            return
        else:
            computer(comp,user)
    
list=[11,2,3,4,5,6,7,8,9,10,10,10]
import random as r
import os
print_logo()
ch=input('Do you wanna play Blackjack? Type "yes" or "no"? ').lower()
while(ch=="yes"):
    main()    
    ch=input('Do you wanna play Blackjack? Type "yes" or "no"? ').lower()
    os.system("cls")  
    print_logo()

if ch=="no":
        print("Good Bye")
        exit(0)
else:
        print("Invalid Choice!")
        exit(0)  







            



        
            
            

            
