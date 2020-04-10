# Problem 55

# If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.
# Not all numbers produce palindroms so quickly. For example,
#   349 + 943 - 1292,
#   1292 + 2921 = 4213
#   4213 + 3124 = 7337
# That is, 349 took three iterations to arrive at a palindrome.

# How many Lychrel numbers are there below ten-thousand?

def reverse_and_add(number):
    reverse = int(str(number)[::-1])
    return number + reverse

def is_lychrel(number, iteration=0):
    iteration += 1
    if (iteration > 50):
        return True
    abc = reverse_and_add(number)
    cba = int(str(abc)[::-1])
    if (abc == cba):
        return False
    else:
        return is_lychrel(abc, iteration)

lychrels = 0
for num in range(10_001):
    if is_lychrel(num):
        lychrels += 1

print(lychrels)