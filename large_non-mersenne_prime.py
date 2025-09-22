# Problem 97

from timeit import time_func

@time_func
def this():
    nmp = 28433 * 2**7830457 + 1
    ltd = nmp % 10**10
    print(ltd)

this()