import random

print('Hello, what is your name?')
name=input()
print('Hi,  ' +str(name)+ ", let's play a game - guess the number.")

print('Well, I am thinking a number between 1 and 20.')
secretNumber=random.randint(1,20)

for i in range(6):
    print('Take a guess.')
    guess=int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break # guess is correct

if guess==secretNumber:
    print('Good job! '+str(name)+', you guessed my number in '+str(i+1)+' guesses!')
else:
    print('Nope. I number I was thinking of was '+str(secretNumber))
