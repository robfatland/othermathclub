import time  
  
def sieve_of_eratosthenes(n):  
    primes = []  
    sieve = [True] * (n + 1)  
    for p in range(2, n + 1):  
        if sieve[p]:  
            primes.append(p)  
            for i in range(p * p, n + 1, p): sieve[i] = False  
    return primes  
  
start_time = time.time()  
primes = sieve_of_eratosthenes(120000)  
end_time = time.time()  
  
print("10,000th prime:", primes[9999])  
print("Execution time: {} seconds".format(end_time - start_time))  
