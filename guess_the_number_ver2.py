import random

print('Hello. What is your name?')
name = input()

secretNumber=random.randint(1,20)
print('Well, ' + name + ', I am thinking of a number between 1 and 20.')

for i in range(6):
    print('take a guess')
    guess=int(input())
    if guess == secretNumber:
        print('yes')
        print('Good job, '+ name + '! You guessed my number in '+ str(i+1) +" guesses.")
        break
    elif guess < secretNumber:
        print('your guess is too low.')
    else:
        print('Your guess is too high.')

if i==5:
    print('Nope. The number I was thinking of was '+str(secretNumber))
