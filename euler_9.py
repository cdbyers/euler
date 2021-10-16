#euler #9



#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a2 + b2 = c2

#For example, 32 + 42 = 9 + 16 = 25 = 52.

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

#just check the whole 1000^3 space

from math import sqrt

def check_all(x):
    for i in range(1, (x//3)+1):
        for j in range(0, (x//2)+1):
            k = sqrt((i ** 2) + (j ** 2))
            if k % 1 == 0:
                if i + j + int(k) == x:
                    return(print(i, " ", j, " ", int(k)))
    return("Zutalors")
                

