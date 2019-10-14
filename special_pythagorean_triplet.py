# Problem 9
#
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

for a in range(1000,0,-1):
    for b in range(1,a):
        c_sqr = a**2 + b**2
        c = c_sqr**.5
        if a + b + c == 1000:
            print(a*b*c)
            exit()

