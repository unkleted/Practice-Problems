# Problem 43
import time
start = time.time()

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

digits = [ i for i in range(10) ]
total = 0
perms = permutations(digits)
for perm in perms:
    n = ''
    for p in perm:
        n += str(p)
    perm = n
    if int(perm[1:4]) % 2 == 0 and int(perm[2:5]) % 3 == 0 and \
        int(perm[3:6]) % 5 == 0 and int(perm[4:7]) % 7 == 0 and \
        int(perm[5:8]) % 11 == 0 and int(perm[6:9]) % 13 == 0 and \
        int(perm[7:10]) % 17 == 0:
        #print('ding',perm)
        total += int(perm)
print(total)

print(time.time() - start)