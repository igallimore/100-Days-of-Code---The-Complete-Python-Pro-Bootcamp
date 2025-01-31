import random

print("Let's play rock, paper, scissors!\n Are you ready?!")

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

# computer_choices = ['rock', 'paper', 'scissors']
computer_choices = [1, 2, 3]
computer = computer_choices[random.randint(0,2)]

human_choice = input ("Make your pick!")

if human_choice == "rock" and computer == 2:
    print(paper)
    print("I win! You lose!")

elif human_choice == "scissors" and computer == 2:
    print(paper)
    print("You win!")

elif human_choice == "paper" and computer == 2:
    print(paper)
    print("It's a tie!")

elif human_choice == "scissors" and  computer == 1:
    print(rock)
    print("You lose!")
elif human_choice == "paper" and computer == 1:
    print(rock)
    print("You win!")
elif human_choice == "rock" and  computer == 1:
    print(rock)
    print("It's a tie!")

elif human_choice == "scissors" and  computer == 3:
    print(scissors)
    print("It's a tie")
elif human_choice == "paper" and  computer == 3:
    print(scissors)
    print("You lose!")
elif human_choice == "rock" and  computer == 3:
    print(scissors)
    print("You win!")




