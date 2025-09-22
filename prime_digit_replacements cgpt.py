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

my_primes = [p for p in primes_less_than(10**7) if p > 10]
set_my_primes = set(my_primes)
print(f"length of my_primes: {len(my_primes)}")
max_found = 0

for prime in my_primes:
    s = str(prime)   # string form of the prime
    digits_of_prime = [int(ch) for ch in s]
    set_digits_of_prime = set(digits_of_prime)

    for digit in set_digits_of_prime:
        indices = tuple(i for i, ch in enumerate(digits_of_prime) if ch == digit)

        # build a format string with {} in the positions we want to replace
        fmt = "".join("{}" if idx in indices else ch
                      for idx, ch in enumerate(s))

        prime_candidates = []
        for replacement in range(10):
            if 0 in indices and replacement == 0:
                continue  # skip leading zero case
            # fill all {} slots with the same replacement digit
            candidate = int(fmt.format(*([replacement] * fmt.count("{}"))))
            prime_candidates.append(candidate)

        found_primes = set(prime_candidates) & set_my_primes
        if len(found_primes) > max_found:
            max_found = len(found_primes)
            print(prime, indices, found_primes)

    if max_found == 8:
        break
