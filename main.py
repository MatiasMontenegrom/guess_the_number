#Number Guessing Game Objectives:
import random
# Include an ASCII art logo.
from art import logo
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
# Allow the player to submit a guess for a number between 1 and 100.
diffycult_level=int(input("Choose a diffycult level:type 1 for easy 2 for hard:  "))
number=random.randint(1,100)
number_user=int(input("Choose a number betwen 1 and 100: "))

lives=0
if diffycult_level==1:
     lives=10
elif diffycult_level==2:
     lives=5
while number != number_user and lives != 0:
     if number_user > number:
          print("Too high.")
     elif number_user < number:
          print("Too low.")
     lives-=1
     if lives==0:
          break
     number_user=int(input(f"You have only {lives} lives left, Choose a number betwen 1 and 100: "))

if lives==0:
     print(f"You lose The number was {number}")
else:
     print("You won!")
     print(f"You got it! The number was {number}")

# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

