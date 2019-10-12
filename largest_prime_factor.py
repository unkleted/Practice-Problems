# Problem 3
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

from math_stuff import prime_factors

number = 600_851_475_143
#number = 13_195

print(prime_factors(number)[-1])