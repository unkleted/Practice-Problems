# Problem 5
# 2520 is the smallest number that can be divided by each of the numbers from 1 
# to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the 
# numbers from 1 to 20?


incriment = 19 * 17 * 13 * 11 * 7 * 5 * 3 * 2
start = incriment

while True:
    if start % 20 == 0 and start % 19 == 0 and start % 18 == 0 and \
        start % 17 == 0 and start % 16 == 0 and  start % 15 == 0 and \
        start % 14 == 0 and start % 13 == 0 and  start % 12 == 0 and \
        start % 11 == 0:
        print(start)
        break
    else:
        start += incriment
        