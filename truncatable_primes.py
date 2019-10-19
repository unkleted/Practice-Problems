# Problem 37

from math_stuff import is_prime

rtruncs = []
def rtruncatable(left=''):
    """Returns a list of right truncatable primes"""
    global rtruncs    
    for right in range(1,10):
        number = left + str(right)
        if (is_prime(int(number))):
            if int(number) > 7: # we're not counting 2, 3, 5, and 7
                rtruncs.append(int(number))
            rtruncatable(number)
both = []
rtruncatable()  # find right primes b/c its a much smaller list
for right in sorted(rtruncs):
    my_flag = True
    r = str(right)[1:]
    while r:
        print(my_flag)
        if not is_prime(int(r)):
            my_flag = False
            break
        r = r[1:]
    if my_flag:
        both.append(right)

print(sum(both))