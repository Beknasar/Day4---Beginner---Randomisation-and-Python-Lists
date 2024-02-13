from random import randint
rock = '''
      _______
---'     ____)
          (_____)
          (_____)
          (____)
---.__(___)
'''

paper = '''
      _______
---'     ____)____
                ______)
              _______)
             _______)
---.__________)
'''

scissors = '''
      _______
---'     ____)____
                ______)
         __________)
          (____)
---.__(___)
'''

#Write your code below this line 👇
choice_list = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = randint(0, 2)
# My answer
#if (user_choice == 0 and computer_choice == 2) or \
#    (user_choice == 1 and computer_choice == 0) or\
#    (user_choice == 2 and computer_choice == 1):
#    print("You win!")
#elif user_choice == computer_choice:
#    print("Draw!")
#else:
#    print("You lose! Don't worry;)")
# Angelas answer
if user_choice >=3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(f"Your chose {choice_list[user_choice]}")
    print(f"Computer chose {choice_list[computer_choice]}")
    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose!")
    elif computer_choice > user_choice:
        print("You lose!")
    elif computer_choice < user_choice:
        print("You win!")
    elif user_choice == computer_choice:
        print("It's a draw!")
