# Problem 58

# Starting with 1 and spiralling anticlockwise in the following way, a square 
# spiral with side length 7 is formed.

# It is interesting to note that the odd squares lie along the bottom right 
# diagonal, but what is more interesting is that 8 of of the 13 numbers lying 
# along both diagonals are prime; that is, a ratio of 8/13 = 62%

# If one complete new layer is wrapped around the spiral above, a square spiral 
# with side length 9 will be formed. If this proces is continued, what is the 
# side length of the square spiral for which the ratio of primes along both 
# diagonals first falls below 10%?

from math_stuff import is_prime

import time
start_time = time.time()

def get_diagonals(number):
    stop = number ** 2 + 1
    step = number - 1
    start = (number - 2)**2 + step
    return [i for i in range(start, stop, step)]
    

diagonals = [1]
primes = 0
num = 3
while True:
    new_layer = get_diagonals(num)
    for p in new_layer:
        if is_prime(p):
            primes += 1
    diagonals.extend(new_layer)
    percent = primes / len(diagonals)
    if percent < .1:
        print(num)
        print(time.time() - start_time)
        exit()
    num += 2
    