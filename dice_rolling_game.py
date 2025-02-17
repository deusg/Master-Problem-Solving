# Dice Rolling Game

import random

#   Loop
while True:
    #  Ask: roll the dice?
    choice = input('Roll the dice? (y/n): ').lower()
    # If user enters y
    if choice == 'y':
    #   Generate two random numbers
        die1 = random.randint(1, 6)   
        die2 = random.randint(1, 6)   
    #   Print them
        print(f'{die1}, {die2}')
    # If user enters n
    elif choice == 'n':
    #   Print thank you message
        print("Thanks for playing!")
    #   Terminate
        break
    # Else
    else:
    #   Print invalid choice
        print("Invalid choice!")
