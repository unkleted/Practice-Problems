# Problem 14
#
# The following iterative sequence is defined for the set of positive integers:
# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following 
# sequence : 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
#
# It can be seen that this sequence (starting at 13 and finishing at 1) 
# contains 10 terms. Although it has not been proved yet (Collatz Problem), it 
# is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.

all_collatz = {}

def collatz_sequence(number):
    """ Returns the length of the collatz chain """
    global all_collatz
    org = number
    if number in all_collatz:
        return all_collatz[number]
    if number == 1:
        return 1
    # I don't know the value, so I'll find the next number in the chain and add
    # one it its value.
    if number % 2 == 0:
        number /= 2
    else:
        number = number * 3 + 1
    all_collatz[org] = 1 + collatz_sequence(number)
    return all_collatz[org]
    
max_chain = 0
chain = 0
magic_number = 0

for i in range(1, 1_000_001):
    chain = collatz_sequence(i)
    if chain > max_chain:
        max_chain = chain
        magic_number = i

print(f"{magic_number} had the longest chain with a length of {max_chain}")