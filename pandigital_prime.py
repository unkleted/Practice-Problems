# Problem 41

from math_stuff import is_prime

def permutations(li):
    """Return a list of permutations for a given list"""
    my_ret_list = []
    if len(li) <= 1:
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

digits = [1,2,3,4,5,6,7,8,9]

while digits:
    d = digits[:]
    print(digits)
    perms = permutations(d)
    perms.sort(reverse=True)
    for perm in perms:
        n = ''
        for p in perm:
            n += str(p)
        perm = int(n)
        if is_prime(perm):
            print(perm)
            exit()
    digits.pop()
    