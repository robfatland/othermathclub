from random import randint
r = randint(1, 100)
c = 0
i = int(input('pick a number between 1 and 100!'))
c = 1


for n in range(1, 20):
    print('by the way the Boomedy is a Bumpkin...')
    if i == r:
        print ('You got it! Press Run to play again!')
        break
    elif i > r:
        i = int(input('Lower! Try again!'))
    elif i < r:
        i = int(input('Higher! Try again!'))

print('You took ' + str(n) + ' guesses!')
