from typing import NewType


def logo_here():
    logo = """
    _____________________
    |  _________________  |
    | | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
    | |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
    |  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
    | | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
    | |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
    | | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
    | |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
    | | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
    | |___|___|___| |___| | | |              | || |              | || |              | || |              | |
    | | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
    | |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
    |_____________________|
    """
    print(logo)

logo_here()

def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2

def main(*argsv):
    num2=float(input("What is the second number? "))
    dict={"+":add(num1,num2),"-":sub(num1,num2),"*":mul(num1,num2),"/":div(num1,num2)}
    for i in dict:
        print(i)
    op=input("Pick an operation: ")
    ans=dict[op]
    print(f"{num1} {op} {num2} = {dict[op]}")
    return ans
    

ch="new"
while(ch=="yes" or ch=="new"):
    if ch=="yes":
        num1=main()
        ch=input(f'Type "yes" to continue calculating with {num1}, or type "new" to start a new calculation: ')
    elif ch=="new":
        import os
        os.system("cls")
        logo_here()
        num1=float(input("What is the first number? "))
        num1=main(num1)
        ch=input(f'Type "yes" to continue calculating with {num1}, or type "new" to start a new calculation: ')
        
if not ch=="yes" or ch=="no":
    print("Invalid choice!")
