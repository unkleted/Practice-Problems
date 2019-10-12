# Problem 4
#
# A palindromic number reads the same both ways. The largest palindrome made 
# from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]

palindromes = []

for x in range(999, 99, -1):
    for y in range(x, 99, -1):
        if (str(x*y) == reverse_string(str(x*y))):
            palindromes.append(x*y)

print(max(palindromes))
