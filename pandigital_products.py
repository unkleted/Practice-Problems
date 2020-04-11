# Problem 32
# We shall say that an n-digit number is pandigital if it makes use of all the 
# digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 
# through 5 pandigital.
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing 
# multiplicand, multiplier, and product is 1 through 9 pandigital.
# Find the sum of all products whose multiplicand/multiplier/product identity 
# can be written as a 1 through 9 pandigital.
# HINT: Some products can be obtained in more than one way so be sure to only 
# include it once in your sum.

from math_stuff import digits_in_int

digits = [i for i in range(1,10)]

def is_pandigital(a,b,c):
    """Returns True if abc is pandigital where c=a*b"""
    global digits
    string = str(a)+str(b)+str(c)
    if len(string) != 9:
        return False
    for d in digits:
        if string.count(str(d)) != 1:
            return False
    return True

products = []
max = 10_000    # 1 digit number * 4 digit number max is 5 digit number.
for a in range(2,max):
    b = a
    while digits_in_int(b*a) < 5:
        if is_pandigital(a,b,a*b):
            products.append(a*b)
            print(a,b)
        b += 1

print(sum(set(products)))
