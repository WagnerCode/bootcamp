import random

from PIL.ImImagePlugin import number

print("This is an interactive guessing game! \n \
You have to enter a number between 1 and 99 to find out the secret number. \n \
Type 'exit' to end the game. \n \
Good luck!")

number = (random.randint(1, 99))

number2 = str(number)
print(number)
print("What's your guess between 1 and 99?")

guess = input()
counter = 1
while(1):
    if guess == '42':
        if guess == number2 and counter == 1:
            print("42 - число вселенной")
            print("You got it on your first try")
            break
        else:
            print("Once again")
            counter += 1
            guess = input()
    elif guess == number2:
        print("Congrats!")
        print(f'You won in {counter} attempts')
        break
    elif guess == '42' and counter == 1:
        print("42 - число вселенной")
        print("You got it on your first try")
        break
    elif guess == 'exit':
        print('Goodbye!')
        break
    else:
        print("Once again")
        counter += 1
        guess = input()
