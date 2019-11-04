# Problem 5
# 2520 is the smallest number that can be divided by each of the numbers from 1 
# to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the 
# numbers from 1 to 20?

from math_stuff import primes_less_than

smallest = 1
up_to = 20

for prime in primes_less_than(up_to + 1):
    exponent = 1
    while prime ** exponent <= up_to:
        smallest *= prime
        exponent += 1

print(smallest)