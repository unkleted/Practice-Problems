# Problem 51
# By replacing the 1st digit of the 2-digit number *3, it turns out that six of 
# the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

# By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit 
# number is the first example having seven primes among the ten generated 
# numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 
# 56993. Consequently 56003, being the first member of this family, is the 
# smallest prime with this property.

# Find the smallest prime which, by replacing part of the number (not 
# necessarily adjacent digits) with the same digit, is part of an eight prime 
# value family.

from math_stuff import primes_less_than

my_primes = [ _ for _ in primes_less_than(10**6) if _ > 10**1 ] 
set_my_primes = set(my_primes)

max_found = 0

for prime in my_primes:
    digits_of_prime = [ int(_) for _ in str(prime) ]
    set_digits_of_prime = set(digits_of_prime)
    for digit in set_digits_of_prime:
        indices = tuple(i for i, x in enumerate(digits_of_prime) if x == digit)
        prime_candidates = []
        for i in range(10):
            new_prime = ""
            if 0 in indices and i == 0:
                continue
            for d_index in range(len(digits_of_prime)):
                if d_index in indices:
                    new_prime += str(i)
                else:
                    new_prime += str(digits_of_prime[d_index])
            prime_candidates.append(int(new_prime))
            
        found_primes = set(prime_candidates) & set_my_primes
        if len(found_primes) > max_found:
            max_found = len(found_primes)
            print(prime, set_digits_of_prime, indices, found_primes)
    if max_found == 8:
        break



# Brute force works but slow. Far too many combos. Be smarter.
# from math_stuff import primes_less_than
# from itertools import combinations
# from math import inf
# from pprint import pprint


# my_primes = set([ _ for _ in primes_less_than(10**6) if _ > 10**1 ])

# most_primes = {}

# for prime in my_primes:
#     digits_of_prime = [ int(_) for _ in str(prime) ]
#     length_of_prime = len(digits_of_prime)
#     most_primes.setdefault(length_of_prime,{"max": 0, "indicies": (), "primes":[], "og_prime": inf })
#     for i in range(1,length_of_prime):
#         for j in combinations(range(length_of_prime), i):
#             prime_candidates = []
#             for k in range(10):
#                 if 0 in j and k == 0:
#                     continue
#                 new_prime = ""
#                 for d in range(length_of_prime):
#                     if d in j:
#                         new_prime += str(k)
#                     else:
#                         new_prime += str(digits_of_prime[d])
#                 prime_candidates.append(int(new_prime))
#             found_primes = set(prime_candidates) & my_primes
#             if len(found_primes) > most_primes[length_of_prime]["max"]:
#                 most_primes[length_of_prime] = {
#                     "max": len(found_primes),
#                     "indicies": j,
#                     "primes": found_primes,
#                     "og_prime": prime
#                 }
#             elif len(found_primes) == most_primes[length_of_prime]["max"] and prime < most_primes[length_of_prime]["og_prime"]:
#                 most_primes[length_of_prime] = {
#                     "max": len(found_primes),
#                     "indicies": j,
#                     "primes": found_primes,
#                     "og_prime": prime
#                 }

# pprint(most_primes)

# {2: {'indicies': (0,),
#      'max': 6,
#      'og_prime': 13,
#      'primes': {73, 43, 13, 83, 53, 23}},
#  3: {'indicies': (1,),
#      'max': 6,
#      'og_prime': 107,
#      'primes': {197, 167, 137, 107, 157, 127}},
#  4: {'indicies': (0, 2),
#      'max': 6,
#      'og_prime': 1009,
#      'primes': {5059, 7079, 2029, 4049, 8089, 1019}},
#  5: {'indicies': (2, 3),
#      'max': 7,
#      'og_prime': 56003,
#      'primes': {56993, 56003, 56773, 56333, 56113, 56663, 56443}},
#  6: {'indicies': (0, 2, 4),
#      'max': 8,
#      'og_prime': 120383,
#      'primes': {121313,
#                 222323,
#                 323333,
#                 424343,
#                 525353,
#                 626363,
#                 828383,
#                 929393}}}