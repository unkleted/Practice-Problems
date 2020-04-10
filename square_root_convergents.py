# Problem 57

# It is possible to show that the square root of two can be expressed as an 
# infinite continued fraction.

# In the first one-thousand expansions, how many fractions contain a numerator 
# with more digits than the denominator?

numerator = 1
denominator = 1
count = 0
for i in range(1_001):
    denom_len = int(len(str(denominator)))
    numer_len = int(len(str(numerator)))
    if numer_len > denom_len:
        count += 1
    next_denom = numerator + denominator
    next_numer = next_denom + denominator
    numerator = next_numer
    denominator = next_denom

print(count)