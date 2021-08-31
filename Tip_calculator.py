print("Welcome to Tip Calculator")
bill=float(input("What was the total bill? "))
tip_per=int(input("What percentage tip would you like to give? "))
num=int(input("How many people to split the bill? "))
tip=(tip_per*bill)/100
tot=bill+tip
pay=tot/num
print(f"Each person should pay {pay}")
