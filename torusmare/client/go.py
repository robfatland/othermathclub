from torus_client import guess

# See the welcome message
print(guess()["message"])

# Submit a guess
g = "42"
print()
print('guess will be ' + str(g))
print()
print(guess(g)["message"])
print()

g = "5050"
print()
print('guess will be ' + str(g))
print()
print(guess(g)["message"])
print()
