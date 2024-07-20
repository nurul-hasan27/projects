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

# Write your code below this line 👇
import random

print("Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
print("Enter your choice :")
choice = int(input())
if (choice == 0):
    print(rock)
elif (choice == 1):
    print(paper)
elif (choice == 2):
    print(scissors)
print("computer's choice:\n")
comp = random.randint(0, 2)
print(comp)
if (comp == 0):
    print(rock)
elif (comp == 1):
    print(paper)
elif (comp == 2):
    print(scissors)

if ((choice == 0 and comp == 0) or (choice == 1 and comp == 1) or (choice == 2 and comp == 2)):
    print("game draw")
elif (choice == 0 and comp == 1):
    print("You lose and computer win")
elif (choice == 0 and comp == 2):
    print("You win and computer lose")
elif (choice == 1 and comp == 0):
    print("You win and computer lose")
elif (choice == 1 and comp == 2):
    print("You lose and computer win")
elif (choice == 2 and comp == 0):
    print("You lose and computer win")
elif (choice == 2 and comp == 1):
    print("You win and computer lose")
else:
    print("Please enter a valid choice")
