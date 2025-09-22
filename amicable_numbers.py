# Problem 21
#
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n 
# which divide evenly into n). If d(a) = b and d(b) = a, where a!=b, then a and
# b are an amicable pair and each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1,2,4,5,10,11,20,22,44,55, and 
# 110 ; therefore d(220) = 284. The proper divisors of 284 are 1,2,4,71, and 
# 142; so d(284)=220.
#
# Evaluate the sum of all the amicable numbers under 10_000.

from math_stuff import all_divisors

def proper_divisors_sum(number) -> int:
    """Returns the sum of proper divisors."""
    proper = sum(all_divisors(number)[:-1])
    return proper

ammicable = []

for a in range(1,10_000):
    if a in ammicable:
        continue
    b = proper_divisors_sum(a)
    if a == proper_divisors_sum(b) and a != b:
        ammicable.append(a)
        ammicable.append(b)

print(sum(ammicable))