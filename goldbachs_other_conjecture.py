# Problem 46
# It was proposed by Christian Goldbach that every odd composite number can be 
# written as the sum of a prime and twice a square.
# It turns out that the conjecture was false.
# What is the smallest odd composite that cannot be written as the sum of a 
# prime and twice a square?

from math_stuff import is_prime

def gen_twice_a_square():
    i = 1
    while True:
        yield (2 * i*i, i)
        i += 1

i = 1
while True:
    i += 2
    found = False
    gen = gen_twice_a_square()
    s, r = next(gen)
    if is_prime(i):
        continue
    # print(i)
    while s < i:
        # print(f"i: {i}, n: {n}")
        if is_prime(i - s):
            print(f"{i} = {i-s} + 2 x {r}**2")
            found = True
            break
        s,r = next(gen)
    if not found:
        print(i)
        break
