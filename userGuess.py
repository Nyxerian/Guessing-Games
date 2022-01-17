import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Try guess the number between 1 and {x}: '))
        if guess < random_number:
            print('Your guess is too low! Try again!')
        elif guess > random_number:
            print('Your guess it too high! Try again!')        
    print(f'Excellent! You guess that the correct number was {random_number}!')

guess(20)