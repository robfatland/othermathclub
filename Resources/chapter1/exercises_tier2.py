# AI in use: True
# Chapter 1, Tier 2 exercises: Loops, logic, remainder
# trinket: [untested] | vscode: [untested]

# --- Exercise 1.4: Is it even? ---
def is_even():
    n = int(input("Give me a number: "))
    if n % 2 == 0:
        print(n, "is even")
    else:
        print(n, "is odd")


# --- Exercise 1.5: Powers table ---
def powers_table():
    for i in range(10):
        print(i, i**2, i**3)


# --- Exercise 1.6: Random choice ---
def random_animals():
    from random import choice
    animals = ["cat", "dog", "fish", "parrot", "hamster"]
    for i in range(5):
        print("You got a", choice(animals))


# --- Exercise 1.7: Skip to my Lou (remainder/modulo) ---
def skip_to_my_lou():
    for i in range(12):
        print("skip " * (i % 3) + "to my Lou")


# --- Exercise 1.8: Triangle of spaces ---
def triangle():
    n = 10
    for i in range(n):
        print(" " * (n - i) + "*" * (2 * i + 1))


# --- Run one exercise at a time ---
# Uncomment the one you want to try:

# is_even()
# powers_table()
# random_animals()
# skip_to_my_lou()
# triangle()
