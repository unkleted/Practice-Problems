# Problem 36
# The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in 
# base 10 and base 2.
# (Please note that the palindromic number, in either base, may not include 
# leading zeros.)

def dec_to_bin(number):
    """ Returns a binary string of the decimal number """
    exp = 0
    while 2**exp < number:
        exp += 1
    bi = ''
    while exp >= 0:
        if number >= 2**exp:
            bi += '1'
            number -= 2**exp
        elif len(bi) > 0:
            bi += '0'
        exp -= 1
    return bi

sum_of_all = 0

for i in range(1,1_000_000):
    if str(i) == str(i)[::-1]:
        my_bi = dec_to_bin(i)
        if my_bi == my_bi[::-1]:
            sum_of_all += i
print(sum_of_all)