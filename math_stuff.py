import math
import itertools
from functools  import reduce

def prime_factors(number) -> list[int]:
    """Returns list of prime factors of number."""
    my_list = []
    if number < 1:
        return my_list
    while number % 2 == 0:
        number //= 2
        my_list.append(2)
    while number % 3 == 0:
        number //= 3
        my_list.append(3)
    i = 5
    while i <= math.sqrt(number):
        while number % i == 0:
            my_list.append(i)
            number //= i
        while number % (i+2) == 0:
            my_list.append(i+2)
            number //= (i+2) 
        i += 6
    if number > 2:
        my_list.append(int(number))

    return my_list


def gen_primes():
    """ Generate and infinite sequence of prime numbers."""
    # Sieve of Eratosthenes
    # Code by David Eppstean, UC Irvine, 28 Feb 2002
    # http://code.activestate.com/recipes/117119/

    # Maps composites to primes witnessing their compositeness. This is memory 
    # efficient, as the siev is not "run forward" indefinitely, but only as long 
    # as required by the curent number being tested

    D = {}
    # The running integer that's checked for primeness
    q = 2
    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't already marked in
            # previous iterations
            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that divide it. Since 
            # we've reached q, we no longer need it in the map, but we'll mark
            # the next multiples of its witnesses to prepare for larger numbers
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1
        

def gen_primes_odd():
    """ Generate and infinite sequence of prime numbers."""
    # Sieve of Eratosthenes
    # Code by David Eppstean, UC Irvine, 28 Feb 2002
    # http://code.activestate.com/recipes/117119/

    # Maps composites to primes witnessing their compositeness. This is memory 
    # efficient, as the siev is not "run forward" indefinitely, but only as long 
    # as required by the curent number being tested
    yield 2
    D = {}
    # The running integer that's checked for primeness
    q = 3
    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't already marked in
            # previous iterations
            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that divide it. Since 
            # we've reached q, we no longer need it in the map, but we'll mark
            # the next multiples of its witnesses to prepare for larger numbers
            for p in D[q]:
                D.setdefault((2*p) + q, []).append(p)
            del D[q]

        q += 2

def slow_all_divisors(number):
    """Returns a list of all natural divisors of a number."""
    my_list = []
    # Brute force every combination up the the sqr root, grabbing factors
    # 2 at a time.
    for i in range(1, int(math.sqrt(number) + 1 )):
        if number % i == 0:
            my_list.append(i)
            my_list.append(int(number/i))
    # Remove duplicates for cases where number is a perfect square.
    return sorted(set(my_list)) 

def all_divisors(number) -> list[int]:
    """Returns a list of all natural divisors of a number."""
    if number == 1: # Edge case for 1 and 0 having no prime factors.
        return [1]
    elif number == 0:
        return []
    pf = prime_factors(number)
    pf_set = set(pf)
    my_lol = [] # temp list of lists
    # Populate my_lol with all combinations of that factor and its exponents
    for factor in pf_set:
        my_tmp_lst = [factor**i for i in range(pf.count(factor) + 1 )]
        my_lol.append(my_tmp_lst)

    my_complete_lst = my_lol.pop() # Grab list from LoL; multiply factors
    while my_lol:
        my_tmp1 = my_lol.pop() # Grab 2nd list.
        my_tmp2 = [] # Place holder. Will put these values into complete_lst
        for o in my_complete_lst:
            for i in my_tmp1:
                my_tmp2.append(o*i)
        my_complete_lst = my_tmp2[:]
    
    return sorted(my_complete_lst)


def all_divisors_again(number) -> list[int]:
    """Returns a list of all natural divisors of a number."""
    if number == 0:
        return []
    if number == 1:
        return [1]

    pf = prime_factors(number)
    tuples = [tuple(f**i for i in range(pf.count(f)+1)) for f in set(pf)]
    divisors = [math.prod(p) for p in itertools.product(*tuples)]
    return sorted(divisors)    
    # if number == 1: # Edge case for 1 and 0 having no prime factors.
    #     return [1]
    # elif number == 0:
    #     return []
    # pf = prime_factors(number)
    # my_lst = []
    # for factor in set(pf):
    #     my_tup = tuple(factor**i for i in range(pf.count(factor) + 1))
    #     my_lst.append(my_tup)

    # # divisors = [math.prod(p) for p in itertools.product(*my_lst)]
    # divisors = [reduce(lambda x, y: x*y, p) for p in itertools.product(*my_lst)]

    # return sorted(divisors)


def primes_less_than(number):
    """Returns a list of prime numbers less than the number given."""
    primes = []
    # not_primes = {}
    # for n in range(2,number):
    #     if n not in not_primes:
    #         primes.append(n)
    #         for i in range(n**2, number, n):
    #             not_primes[i] = 42
    pg = gen_primes_odd()
    n = next(pg)
    while n < number:
        primes.append(n)
        n = next(pg)
    return primes

def is_prime(number):
    """Returns True if number is prime."""
    if number <= 1: 
        return False
    if number > 2 and number % 2 == 0:
        return False
    if number > 3 and number % 3 == 0:
        return False
    i = 5
    while i <= math.sqrt(number):
        if number % i == 0 or number % (i+2) == 0:
            return False
        i+=6
    return True

def factorial(number):
    """Returns the factorial of number"""
    if number <= 1:
        return 1
    return number * factorial(number -1)

def greatest_common_divisor(a,b):
    """Returns the greatest common divisor"""
    while b != 0:
        a, b = b, a % b
    return a

def digits_in_int(number):
    """Returns the number of digits in a given integer"""
    return int(math.log10(number))+1