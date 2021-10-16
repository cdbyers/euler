#Euler #3

#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

def isprime(x)
    result = True
    for i in tqdm(range(2, (x // 2) + 1)):
        if(x % i == 0):
            result = False
            break
    return(result)

#too slow for 79999999999


def isprime(x):
    if(x <= 3):
        return(x > 1)
    if(x % 2 == 0 or x % 3 == 0):
        return(False)
    i = 5 
    while i ** 2 < x:
        if x % i == 0 or x % (i + 2) == 0:
            return False
        i += 6
    return True

#adapted from wikipedia article on primality tests

def makeprimelist(n):
    primes = []
    for i in range(0, n + 1):
        if isprime(i):
            primes.append(i)
    return(primes)

def prime_factor(x):
    factors = []
    target = x
    i = 1
    while True:
        checklist = makeprimelist(10 ** i)
        for j in checklist:
            if isprime(target):
                factors.append(int(target))
                return(factors)
            if(target % j == 0):
                factors.append(j)
                target = target / j
        i += 1


answer = max(prime_factor(600851475143))
