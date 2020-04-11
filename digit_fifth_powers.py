# Problem 30
# Surprisingly there are only three numbers that can be written as the sum of 
# fourth powers of their digits:

# 1634 = 14 + 64 + 34 + 44
# 8208 = 84 + 24 + 04 + 84
# 9474 = 94 + 44 + 74 + 44
# As 1 = 14 is not a sum it is not included.

# The sum of these numbers is 1634 + 8208 + 9474 = 19316.

# Find the sum of all the numbers that can be written as the sum of fifth 
# powers of their digits.

from math_stuff import digits_in_int

my_list = []
i = 2
while i < digits_in_int(i) * 9**5:
    number = str(i)
    total = 0
    for n in number:
        total += int(n)**5
    if total == i:
        my_list.append(i)
    i += 1
print(sum(my_list))