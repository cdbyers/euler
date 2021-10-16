# Euler #5

#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def find(x):
    nx_n = 1 
    incr = 1 
    step = 1
    while nx_n <= x:
        if(incr % nx_n == 0):
            step = max(incr, 1)
            nx_n += 1
            if(nx_n > x):
                return(incr)
            continue
        incr += step
    return(incr)

answer = find(20)

