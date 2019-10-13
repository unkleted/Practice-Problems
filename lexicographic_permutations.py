#!/usr/env python3ts
# Problem 24
#
# A permutation is an ordered arrangement of objects. For example, 3124 is one
# possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
# are listed numerically or alphabetically, we call it lexicographic order. The
# lexicographic permutations of 0, 1 and 2 are:
# 012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits
# 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
import time
start_time = time.time()

def permutations(li):
    """Return a list of permutations for a given list"""
    my_ret_list = []
    if len(li) == 1:
        my_ret_list.append(li)
    else:
        my_val = li.pop(0)
        my_tmp_lsts = permutations(li)
        for lst in my_tmp_lsts:
            for i in range(len(lst)+1):
                tmp = lst[:]
                tmp.insert(i,my_val)
                my_ret_list.append(tmp)
    return my_ret_list

nums = [0,1,2,3,4,5,6,7,8,9]
perms = permutations(nums)
perms.sort()
print(perms[999999])

print(time.time() - start_time)
