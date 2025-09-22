# Problem 24 v2
#
# A permutation is an ordered arrangement of objects. For example, 3124 is one
# possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
# are listed numerically or alphabetically, we call it lexicographic order. The
# lexicographic permutations of 0, 1 and 2 are:
# 012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits
# 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

from math_stuff import factorial

numbers = list(range(10))
position = 1_000_000  # 1-based

mutation = ''

while numbers:
    n = len(numbers)
    if n == 1:
        mutation += str(numbers.pop())
        break
    fact = factorial(n-1)
    index = (position-1) // fact
    mutation += str(numbers.pop(index))
    position -= index * fact

print(mutation)


# numbers = [0,1,2,3,4,5,6,7,8,9]
# numbers.sort()
# position = 1_000_000

# if position > factorial(len(numbers)):
# 	print('nope :(')
# 	exit()

# mutation = ''
# while len(numbers) > 1:
# 	j = position % factorial(len(numbers))
# 	k = 0
# 	index = 0
# 	while k < j:
# 		index += 1
# 		k = factorial(len(numbers)-1) * index
# 	mutation += str(numbers.pop(index-1))

# mutation += str(numbers.pop())
# print(mutation)