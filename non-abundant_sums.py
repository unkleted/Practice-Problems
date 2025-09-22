# Problem 23
#
# A perfect number is a number for which the sum of its proper divisors is 
# exactly equal to the number. For example, the sum of the proper divisors of 
# 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less than 
# n and it is called abundant if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest 
# number that can be written as the sum of two abundant numbers is 24. By 
# mathematical analysis, it can be shown that all integers greater than 28123 
# can be written as the sum of two abundant numbers. However, this upper limit 
# cannot be reduced any further by analysis even though it is known that the 
# greatest number that cannot be expressed as the sum of two abundant numbers 
# is less than this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum 
# of two abundant numbers.

# import time
from timeit import time_func
# start = time.time()
from math_stuff import all_divisors

@time_func
def main():
    upper = 28123

    # find all abundant numbers:
    abundants = []
    for number in range(1,upper+1):
        sum_of_divisors = sum(all_divisors(number)[:-1])
        if sum_of_divisors > number:
            abundants.append(number)

    # find sums of abundant pairs
    abun_pairs = {}
    while abundants:
        for a in abundants:
            abun_pairs[abundants[0] + a] = 0
        abundants.pop(0)

    # look for ints that aren't in abun_pairs
    sum_of_ints = 0
    for i in range(1,upper):
        if i not in abun_pairs:
            sum_of_ints += i

    print(sum_of_ints)

# print(time.time() - start)
if __name__ == "__main__":
    main()