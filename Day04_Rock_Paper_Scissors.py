rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
list=[rock,paper,scissor]
import random as r
choice=int(input("Enter your choice: Type 0 for rock, Type 1 for paper, Type 2 for scissors \n"))
if choice>2 or choice<0:
    print("Invalid choice")
    exit(0)
print(f"You choose: {list[choice]}")
com=r.randint(0,2)
print(f"Computer choose: {list[com]}")
if choice==com:
    print("Draw")
if choice==2 and com==0:
    print("You lose!")
elif choice<com:
    print("You lose!")
elif choice>com:
    print("You win!")
