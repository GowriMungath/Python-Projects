logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print("Welcome to Secret Audit Online")
ch="yes"
bidders={}
while(ch=="yes"):
    name=input("What is your name? ")
    bid=int(input("What is your bid? "))
    bidders[name]=bid
    ch=input("Do you want to add more people to bid? Type Yes or No. ").lower()
    import os 
    os.system("cls")

highest=0
winner=""
for i in bidders:
    if(bidders[i]>highest):
        highest=bidders[i]
        winner=i

print(f"The winner is {winner} with a bid of Rs.{highest}.")





