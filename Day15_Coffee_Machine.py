
import Coffee_machine_details as c
import os
from time import sleep
coffee= ("""
    ( (
    ) )
  ........
  |      |]
  \      /    
   `----' """)
def money():
    q=float(input("How many quarters? "))
    d=float(input("How many dimes? "))
    n=float(input("How many nickles? "))
    p=float(input("How many pennies? "))
    dollars=(q*0.25)+(d*0.10)+(n*0.05)+(p*0.01)
    return dollars

def todo():
    sleep(3)  
    os.system("cls")
    
print(coffee)
print("Coffee Machine Turned On ✔️")
todo()
choice="y"
b="in"

while(choice=="y"):

    b="in"
    print(coffee)
    ch=input("What would you like? (espresso/latte/cappuccino): ").lower()
    print(ch+" costs $"+str(c.MENU[ch]["cost"])+".")
    print("Current Resources:")
    print(c.resources)
    print("Required Resources for "+ch+": ")
    print(c.MENU[ch]["ingredients"])

    for i in c.MENU[ch]["ingredients"]:
        if (c.resources[i]<c.MENU[ch]["ingredients"][i]):
            print(f"Sorry there is no enough {i}!👎")
            todo()
            b="out"
            break
    if b=="out":
        choice=input('Do you want to continue buying coffee? Type "Y" for Yes or "N" for No: ').lower()
        if choice=='y':
            continue
        else:
            break

    print("Insert Coins 💰")
    dollars=round(money(),2)
    while(dollars<c.MENU[ch]["cost"]):
            print("You entered $"+str(dollars)+".")
            ans=input("Sorry there is no enough coins!👎 Insert more coins? Type 'Y' for Yes or 'N' for No: ")
            if ans=='y':
               dollars+=money()
            else:
                print("Your entered money has been refunded.")
                dollars=0
                break
    if(dollars>c.MENU[ch]["cost"]):
            change=dollars-c.MENU[ch]["cost"]
            print(f"Here is your change:${round(change,2)}")
    if(dollars>=c.MENU[ch]["cost"]):
        c.resources["water"]-=c.MENU[ch]["ingredients"]["water"]
        c.resources["coffee"]-=c.MENU[ch]["ingredients"]["coffee"]
        if ch!="espresso":
            c.resources["milk"]-=c.MENU[ch]["ingredients"]["milk"]
        print("Here is your "+ch+".☕ Enjoy!")
        
    choice=input('Do you want to continue buying coffee? Type "Y" for Yes or "N" for No: ').lower()
    os.system("cls")

print("Coffee machine turned off!❌")
