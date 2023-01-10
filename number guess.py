"""
number guess
"""
from random import randint

print("guess the number between 1 - 10",
      "you have 3 chances to make a correct guess",
      "let's begin", sep='\n')
interest = 1
while interest != '0':
    number = randint(1, 10)
    count = 3
    while count > 0:
        print('------------------')
        guess = int(input("enter your guess: "))
        if number == guess:
            print("yayyyyy you guessed it")
            break
        else:
            count -= 1
            print("oops!!!...that's not correct")
            print(f'you have {count} chance(s) to go')
    else:
        print(f'\n\nThe number was {number}')
        print("\n\n\nwanna try again?")
        print("press any key to continue / 0 to exit")
        interest = input()


