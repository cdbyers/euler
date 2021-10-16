#Euler 4

#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

import math

def is_pal(x):
    str_x = str(x)
    for i in range(0, len(str_x) // 2):
        if str_x[i] != str_x[-(i + 1)]:
            return(False)
    return(True)

def check(x):
    i = 0
    pals = []
    while i <= x:
       for j in range(i, x + 1):
           num = i * j
           if(is_pal(num)):
               pals.append(num)
       i += 1
    if(len(pals) > 0):
        return(max(pals))
    else:
        return(0)

answer = check(999)

