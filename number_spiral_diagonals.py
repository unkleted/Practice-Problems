# Problem 28
# Starting with the number 1 and moving to the right in a clockwise direction a 
# 5 by 5 spiral is formed as follows:
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
# It can be verified that the sum of the numbers on the diagonals is 101.

# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral 
# formed in the same way?

def count_diags(stop,step,place):
    part_sum = 0
    while place != stop**2:
        place += step
        part_sum += place
    return part_sum

my_dict = {
    i+1:i for i in range(2, 1_001 + 1, 2)
}

my_place = 1
sum = 1

for k,v in my_dict.items():
    sum += count_diags(k,v,my_place)
    my_place = k**2

print(sum)
