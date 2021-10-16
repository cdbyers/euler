# Euler #6


#The sum of the squares of the first ten natural numbers is,

#The square of the sum of the first ten natural numbers is,

#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is


#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sq_py(x):
    return(((x ** 3) / 3) + ((x ** 2) / 2) + (x / 6))

def add_up(x):
    return((x * (x +1)) / 2)

def add_range(x, y):
    return(((y - x) * x) + (((y - x) * (y - x + 1)) / 2))

answer = (add_up(100) ** 2) - sq_py(100)

