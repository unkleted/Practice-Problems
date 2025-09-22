from math_stuff import primes_less_than
from itertools import combinations

def find_sequence():
    primes = [p for p in primes_less_than(10_000) if p > 999]
    prime_set = set(primes)

    # group primes by digit signature
    groups = {}
    for p in primes:
        key = "".join(sorted(str(p)))
        groups.setdefault(key, []).append(p)

    # print(groups)

    # check each group for arithmetic sequences
    for group in groups.values():
        if len(group) < 3:
            continue
        group.sort()
        for a, b, c in combinations(group, 3):
            if b - a == c - b and {a, b, c} != {1487, 4817, 8147}:
                return str(a) + str(b) + str(c)

print(find_sequence())
