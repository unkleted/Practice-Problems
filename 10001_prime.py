# Problem 7
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see 
# that the 6th prime is 13.
#
# What is the 10_001st prime number?

from math_stuff import is_prime

primes = [2,3]
i = 5
while len(primes) < 10_001:
    if is_prime(i):
        primes.append(i)
    if is_prime(i+2):
        primes.append(i+2)
    i += 6

print(primes[-1])