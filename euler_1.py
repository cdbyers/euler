#Euler #1: 

#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

#Find the sum of all the multiples of 3 or 5 below 1000.

#Answer is multiples of 3 + multiples of 5 - multiples of both i.e. 15

#sum of any incrementing group of numbers is 1/2 * 

def brute_force_fn(x):
    counter = 0
    for i in range(0, x):
        if i % 5 == 0 or i % 3 == 0:
            counter = counter + i
    return counter

def br_base(x):
    counter = 0
    for i in range(0, x):
        counter = counter + i 
    return(counter)

def incr(x):
    return((x * (x +1)) / 2)


def one_divisor(n, x):
    instances = n // x
    return(incr(instances) * x)

def two_divisor(n, x, y):
    under_n = n - 1 
    instances_x = under_n // x
    instances_y = under_n // y
    instances_intersection = under_n // (x * y)
    sum_x = incr(instances_x) * x
    sum_y = incr(instances_y) * y
    sum_inter = incr(instances_intersection) * (x * y)
    return(sum_x + sum_y - sum_inter)

answer = two_divisor(1000, 3, 5)

