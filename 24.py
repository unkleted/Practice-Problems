# Problem 24 v2
#
# Instead of computing every permutation, this will only compute the 
# permutation at the requested position

from math_stuff import factorial

import time
start_time = time.time()

numbers = [0,1,2,3,4,5,6,7,8,9]
numbers.sort
position = 1_000_000

if position > factorial(len(numbers)):
	print('nope :(')
	exit()

mutation = ''
while len(numbers) > 1:
	j = position % factorial(len(numbers))
	k = 0
	index = 0
	while k < j:
		index += 1
		k = factorial(len(numbers)-1) * index
	mutation += str(numbers.pop(index-1))

mutation += str(numbers.pop())
print(mutation)

print(time.time() - start_time)