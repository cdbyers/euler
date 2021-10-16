#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

#Find the sum of all the primes below two million.

#Make function to guage prime-ness

def isprime(x):
    if(x <= 3):
        return(x > 1)
    if(x % 2 == 0 or x % 3 == 0):
        return(False)
    #note we're starting i at 5, not 6 - since we're comparing i^2, but max factor is sqrt(x), i has to be minimum that we're testing. This is a 
    i = 5 
    while i ** 2 <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return(False)
        i += 6
    return(True)

def makeprimelist(n):
    primes = 0 
    for i in range(0, n + 1):
        if isprime(i):
            primes += i
    return(primes)

