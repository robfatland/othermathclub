# AI in use: True
# Chapter 1, Tier 3 exercises: Functions and libraries
# trinket: [untested] | vscode: [untested]

# --- Exercise 1.9: Is it prime? ---
def is_prime(n):
    """Return True if n is prime, False otherwise."""
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def show_primes():
    for k in range(2, 50):
        if is_prime(k):
            print(k, end=" ")
    print()


# --- Exercise 1.10: Factorial ---
def factorial(n):
    """Return n! (n factorial)."""
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result


def show_factorials():
    for k in range(10):
        print(k, "! =", factorial(k))


# --- Exercise 1.11: Alternating sign sum ---
def alternating_sum(n):
    """Return 1 - 2 + 3 - 4 + ... up to n."""
    total = 0
    sign = 1
    for i in range(1, n + 1):
        total = total + sign * i
        sign = sign * -1
    return total


def show_alternating():
    print("alternating_sum(10) =", alternating_sum(10))
    print("alternating_sum(100) =", alternating_sum(100))
    print("alternating_sum(1000) =", alternating_sum(1000))


# --- Exercise 1.12: Timing how long something takes ---
def timing_demo():
    from time import time
    start = time()
    total = 0
    for i in range(1000000):
        total = total + i
    end = time()
    print("Sum of 0 to 999999 =", total)
    print("That took", round(end - start, 4), "seconds")


# --- Run one exercise at a time ---
# Uncomment the one you want to try:

# show_primes()
# show_factorials()
# show_alternating()
# timing_demo()
