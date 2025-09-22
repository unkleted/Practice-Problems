# Problem 49
# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms 
# increases by 3330, is unusual in two ways: (i) each of the three terms are 
# prime, and, (ii) each of the 4-digit numbers are permutations of one another.

# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, 
# exhibiting this property, but there is one other 4-digit increasing sequence.

# What 12-digit number do you form by concatenating the three terms in this 
# sequence?

from math_stuff import primes_less_than
from itertools import permutations

def get_permutations(number: int) -> list[int]:
    ret_list = []
    # convert int into list of str
    list_of_num = [ _ for _ in str(number) ]
    for perm in set(permutations(list_of_num)):
        # concatenate list of digits back into 4 digit numbers
        cat = ""
        for _ in perm:
            cat += _
        ret_list.append(int(cat))
    return ret_list


my_4digit_primes = [ _ for _ in primes_less_than(10_000) if _ > 999 ]


for i in range(1_000, 3_333, 2):
    for prime in my_4digit_primes:
        perms = get_permutations(prime)
        p1 = prime + i
        p2 = prime + (2 * i)
        if (p1 in perms and p2 in perms) and (p1 in my_4digit_primes and p2 in my_4digit_primes):
            print(f"i:{i} -> {prime}, {p1}, {p2}")

