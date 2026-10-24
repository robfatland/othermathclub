from random import choice, randint

# let's play 10,000 games with "no switch" strategy
# g = goat
# m = a million dollars
# c = the door the player chooses
# doors are numbered 1, 2, 3

n_games = 10000
n_wins = 0
for n in range(n_games):
    m = randint(1, 3)
    c = randint(1, 3)
    if c == m: 
        n_wins = n_wins + 1

print('We played', n_games, 'games of "stay" (no-switch) Monty Hall, and won', n_wins, 'games.')
print('The stay strategy has a success ratio of', n_wins/n_games)

# Now when we play the game: We choose one door; and then we switch doors when we get the chance

n_games = 10000
n_wins = 0
for n in range(n_games):
    m = randint(1, 3)
    c = randint(1, 3)
    if not c == m: 
        n_wins = n_wins + 1

print('We played', n_games, 'games of "switch" Monty Hall, and won', n_wins, 'games.')
print('The switch strategy has a success ratio of', n_wins/n_games)

