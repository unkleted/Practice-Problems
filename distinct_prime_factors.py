# Problem 47
# The first two consecutive numbers to have two distinct prime factors are:
# 14 = 2 x 7
# 15 = 3 x 5
# The first three consecutive numbers to have three distinct prime factors are:
# 644 = 2**2 x 7 x 23
# 645 = 3 x 5 x 43
# 646 = 2 x 17 x 19
# Find the first four consecutive integers to have four distinct prime factors 
# each. What is the first of these numbers?

from collections import deque
from math_stuff import prime_factors

unique = 4
window = deque(maxlen=unique)  # keeps last 4 results

i = 644
while True:
    pf = set(prime_factors(i))  # only distinct factors matter
    window.append((i, len(pf)))
    
    if len(window) == unique and all(count == unique for _, count in window):
        print([num for num, _ in window])
        break
    
    i += 1


# from math_stuff import prime_factors

# unique = 4

# prev_3 = (0,[])
# prev_2 = (0,[])
# prev_1 = (0,[])
# current = (0,[])
# i = 644
# while True:
#     prev_3 = prev_2
#     prev_2 = prev_1
#     prev_1 = current
#     pf = prime_factors(i)
#     current = len(set(pf)), i, pf
#     if (unique == current[0] and unique == prev_1[0] and unique == prev_2[0] and unique == prev_3[0]):
#         print(current[1], prev_1[1], prev_2[1], prev_3[1])
#         break
#     i += 1