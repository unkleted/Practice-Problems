# Problem 10
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17
#
# Find the sum of all the primes below two million

from math_stuff import primes_less_than

print(sum(primes_less_than(2_000_000)))