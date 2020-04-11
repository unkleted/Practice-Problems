# Problem 63

# The 5-digit number, 16807=7**5, is also a fifth power. Similarly, the 9-digit 
# number, 134217728=8**9, is a ninth power. How many n-digit positive integers 
# exist which are also an nth power?

from math_stuff import digits_in_int

powerful_digits = []

for i in range(1, 10):  # only single digit numbers
    for e in range(1, 22): # 9**22 is 21 digits, so we can stop there
        if digits_in_int(i**e) == e:
            powerful_digits.append(i**e)

print(len(set(powerful_digits)))