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
if choice==0:
    print(f"You choose: {rock}")
elif choice==1:
    print(f"You choose: {paper}")
elif choice==2:
    print(f"You choose: {scissor}")
com=r.choice(list)
print(f"Computer choose: {com}")
if choice==0 and com==scissor:
    print("You win!")
elif choice==0 and com==paper:
    print("You lose!")
elif choice==0 and com==rock:
    print("Draw!")
elif choice==1 and com==scissor:
    print("You lose!")
elif choice==1 and com==rock:
    print("You win!")
elif choice==1 and com==paper:
    print("Draw")
elif choice==2 and com==paper:
    print("You win!")
elif choice==2 and com==rock:
    print("You lose!")
elif choice==2 and com==scissor:
    print("Draw")
     
