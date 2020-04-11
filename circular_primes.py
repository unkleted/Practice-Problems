# Problem 35
# The number, 197, is called a circular prime because all rotations of the 
# digits: 197, 971, and 719, are themselves prime.
# There are thirteen such primes below 100: 
# 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# How many circular primes are there below one million?

import math_stuff

my_primes = math_stuff.primes_less_than(1_000_000)
my_circles = [2,5]  # only prime numbers to end in 2 or 5.

for prime in my_primes:
    numbers = [int(x) for x in str(prime)]
    # skip if prime has digit that a prime number cannot end with.
    if 0 in numbers or 2 in numbers or 4 in numbers or 5 in numbers or \
        6 in numbers or 8 in numbers:
        continue
    my_flag = True
    p = prime
    for i in range(math_stuff.digits_in_int(p)):
        n = str(p)[-1] + str(p)[:-1]
        p = int(n)
        if p not in my_primes:
            my_flag = False
    if my_flag:
        my_circles.append(prime)  

print(len(my_circles))