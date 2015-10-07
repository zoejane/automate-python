print('How many cats do you hanve?')
numCats =input()
try:
    if int(numCats) >=4:
        print('That is a lot of cats.')
    elif int(numCats) >=0:
        print('That is not that many cats.')
    else:
        print('You did not enter a valid number.')
except ValueError:
    print('You did not enter a number.')
