# Sanjay Adhith

# Singapore, Hillview

# This file contains a program which
# gives a prime factorisation for a given
# factorial number.

# This technique is mostly of academic
# interest though I suppose that it makes
# for a decent programming exercise.

import sympy, math

def multiplicity(p, n):
    current = p
    sum = 0
    while math.floor(n/current) != 0:
        sum += math.floor(n/current)
        current *= p
    return sum


def factors_of_factorial(n):
    primes = sympy.primerange(0,n)
    for i in primes:
        print(i, multiplicity(i,n))
        
print(factors_of_factorial(20))

# I can't think of any practical use for
# this program!
