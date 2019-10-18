# Problem 34
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Find the sum of all numbers which are equal to the sum of the factorial of 
# their digits.
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

# 7*9! is a 7 digit number. 8*9! is also a 7 digit number so no answer will be 
# greater than 7 digits.

from math_stuff import factorial

def sum_of_fact_of_dig(number):
    """ Returns the sum of the factorial of numbers digits """
    ret_sum = 0
    for d in str(number):
        ret_sum += factorial(int(d))
    return ret_sum

upper_bound = 7 * factorial(9)  
all_sums = 0
for i in range(10,upper_bound + 1):
    if i == sum_of_fact_of_dig(i):
        all_sums += i
print(all_sums)