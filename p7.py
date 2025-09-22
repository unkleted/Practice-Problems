# Problem 7
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see 
# that the 6th prime is 13.
#
# What is the 10_001st prime number?


from math_stuff import is_prime, gen_primes, gen_primes_odd
from miller_rabin import isPrime
from timeit import time_func


@time_func
def gen_7(num: int):
    x = gen_primes()
    for _ in range(num):
        next(x)
    print(next(x))


@time_func
def no_gen_7(num: int):
    primes = [2,3]
    i = 5
    while len(primes) < num + 1:
        if is_prime(i):
            primes.append(i)
        if is_prime(i+2):
            primes.append(i+2)
        i += 6

    print(primes[-1])


@time_func
def no_gen_rm_7(num: int):
    primes = [2,3]
    i = 5
    while len(primes) < num + 1:
        if isPrime(i):
            primes.append(i)
        if isPrime(i+2):
            primes.append(i+2)
        i += 6

    print(primes[-1])

@time_func
def odd_gen_7(num: int):
    x = gen_primes_odd()
    for _ in range(num):
        next(x)
    print(next(x))


def main():
    num = 1_000_001
    
    no_gen_7(num)
    no_gen_rm_7(num)
    gen_7(num)
    odd_gen_7(num)


if __name__ == "__main__":
    main()