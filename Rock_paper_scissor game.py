#Rock paper scissor game
import random

rock = '''
                               888
                               888
                               888
        888d888 .d88b.  .d8888b888  888
        888P"  d88""88bd88P"   888 .88P
        888    888  888888     888888K
        888    Y88..88PY88b.   888 "88b
        888     "Y88P"  "Y8888P888  888
'''
paper = '''
        8b,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYba, 8b,dPPYba,
        88P'    "8a ""     `Y8 88P'    "8a a8P_____88 88P'   "Y8
        88       d8 ,adPPPPP88 88       d8 8PP""""""" 88
        88b,   ,a8" 88,    ,88 88b,   ,a8" "8b,   ,aa 88
        88`YbbdP"'  `"8bbdP"Y8 88`YbbdP"'   `"Ybbd8"' 88
        88                     88
        88                     88

'''
scissor = '''
              _ ,/'
      (_).  ,/'
       _  ::
      (_)'  `\.
               `\.

            '''

game_images = [rock,paper,scissor]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor: \n"))
if user_choice >= 0 and user_choice <= 2:
    print(game_images[user_choice])
comp_choice = random.randint(0,2)
print(f"computer chose: ")
print(game_images[comp_choice])
if user_choice>=3 or user_choice<0:
    print("Wrong input, you lose")
elif user_choice == 0 and comp_choice == 2:
    print("You win")
elif comp_choice ==0 and user_choice ==2:
    print("You lose")
elif user_choice>comp_choice:
    print("You win")
elif comp_choice> user_choice:
    print("You lose")
elif comp_choice == user_choice:
    print("It's a draw")

