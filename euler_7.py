# Euler #7

#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10 001st prime number?

def is_prime(x):
    if(x <= 3):
        return(x > 1)
    if((x % 2 == 0) | (x % 3 == 0)):
        return(False)
    counter = 5 
    while(counter ** 2 <= x):
        if((x % counter == 0) | (x % (counter + 2) == 0)):
            return(False)
        counter += 6
    return(True)


def prime_list(n):
    primes = []
    i = 1 
    while(i <= 6):
        if(is_prime(i)):
            primes.append(i)
        if(len(primes) == n):
            return(primes)
        i += 1
    switch = 1
    while(len(primes) < n):
        if(is_prime(i)):
            primes.append(i)
        if(switch > 0):
            i += 4 
        else:
            i += 2
        switch = switch * -1
    return(primes)

answer = max(prime_list(10001))        






