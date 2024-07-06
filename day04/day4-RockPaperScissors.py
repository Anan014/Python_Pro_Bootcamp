import random
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

#Write your code below this line 👇
user = int(input("What do you choose? type 0 for Rock, 1 for Papaer or 2 for Scissors: "))
if user == 0:
    print(rock)
elif user == 1:
    print(paper)
elif user == 2:
    print(scissors)

if user > 3 or user < 0:
    print("You typed an invalid number, you lose!")
else:
    computer = random.randint(0,2)
    print("Computer chose")
    if computer == 0:
        print(rock)
    elif computer == 1:
        print(paper)
    elif computer == 2:
        print(scissors)

    if user == 0:
        if computer == 0:
            print("Draw!")
        elif computer == 1:
            print("Computer win!")
        elif computer == 2:
            print("You win!")
    elif user == 1:
        if computer == 0:
            print("You win!")
        elif computer == 1:
            print("Draw!")
        elif computer == 2:
            print("Computer win!")
    elif user == 2:
        if computer == 0:
            print("Computer win!")
        elif computer == 1:
            print("You win!")
        elif computer == 2:
            print("Draw!")
