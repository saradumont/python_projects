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
import random

game_images =[rock, paper, scissors]


print("Welcome, to the game rock, paper, scissors!")

input = int(input("Ready? type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))

print(game_images[input])

computer = random.randint(0,2)

print("Computer choose:")

print(game_images[computer])

if input > 2 or input < 0:
  print("Invalid number you loose!")
elif input == computer:
  print("It's a tie.")
elif input == 2 and computer == 0:
  print("You loose!")
elif input == 0 and computer == 2:
  print("You win!")
elif input > computer:
  print("You win!")
elif computer > input:
  print("You loose!")

else:
  print("You win!")