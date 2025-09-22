# Problem 33
# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in 
# attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is 
# correct, is obtained by cancelling the 9s.

# We shall consider fractions like, 30/50 = 3/5 to be trivial examples.

# There are exactly four non-trivial examples of this type of fraction, less 
# than one in value, and containing two digits in the numerator and denominator.

# If the product of these four fractions is given in its lowest common terms, 
# find the value of the denominator.

from math_stuff import greatest_common_divisor

num_prod = 1
den_prod = 1

for denominator in range(10, 100):
    for numerator in range(10, denominator):
        if numerator % 10 == 0 and denominator % 10 == 0:
            continue

        common_digits = set(str(numerator)) & set(str(denominator))
        for d in common_digits:
            simp_num = int(str(numerator).replace(d, '', 1))
            simp_den = int(str(denominator).replace(d, '', 1))
            if simp_den == 0:
                continue
            if numerator * simp_den == denominator * simp_num:  # avoids floats
                num_prod *= numerator
                den_prod *= denominator

g = greatest_common_divisor(num_prod, den_prod)
print(den_prod // g)
