# AI in use: True
# Chapter 1, Tier 1 exercises: Print, input, countdown
# trinket: [untested] | vscode: [untested]

# --- Exercise 1.1: Hello ---
def hello():
    print("Hello, world!")
    name = input("What is your name? ")
    print("Nice to meet you, " + name)


# --- Exercise 1.2: Favorite number ---
def favorite_number():
    s = input("Enter your favorite number: ")
    n = int(s)
    print(n - 5, "is five less than your favorite number")
    print(n + 5, "is five more than your favorite number")
    print(n * 2, "is double your favorite number")


# --- Exercise 1.3: Countdown ---
def countdown():
    from time import sleep
    for i in range(10, 0, -1):
        print(i)
        sleep(0.5)
    print("BLAST OFF!")


# --- Run one exercise at a time ---
# Uncomment the one you want to try:

# hello()
# favorite_number()
# countdown()
