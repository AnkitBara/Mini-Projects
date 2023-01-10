"""
Dice - mini project
"""
from random import randint
choice = input("press any key start the Game!! ")
while choice != 0:
    print('press any key to roll the dice \n press 0 to exit: ')
    choice = input()
    num1, num2 = randint(1, 6), randint(1, 6)
    print("\n\nit's lucky.....\n")
    print(f'----->  {num1} {num2}  <-----')
    print(end='\n\n')
