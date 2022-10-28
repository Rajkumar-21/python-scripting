import random
import sys

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user = int(input("What do you chose? Type 0 for Rock, 1 for paper, 2 for scissors."))
computer = random.randint(0,2)

if user == 0:
    print(rock)
elif user ==1:
    print(paper)
elif user==2:
    print(scissors)
else:
    print("Warning: Please enter 0 for Rock, 1 for paper, 2 for scissors. ")
    sys.exit()

print(f'You chose {user}')
print(f'Computer chose {computer}')



if computer == 0:
    print(rock)
elif computer ==1:
    print(paper)
elif computer==2:
    print(scissors)

if user == 0:
    if computer ==0:
        print("Match draw!")
    elif computer == 1:
        print("Computer Wins :(")
    elif computer == 2:
        print("You Win!")

elif user ==1:
    if computer ==0:
        print("Computer Wins :(")
    elif computer == 1:
        print("Match draw!")
    elif computer == 2:
        print("You Win!")

elif user == 2:
    if computer ==0:
        print("Computer Wins :(")
    elif computer == 1:
        print("You Win!")
    elif computer == 2:
        print("Match Draw!")