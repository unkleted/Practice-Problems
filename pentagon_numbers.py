# Problem 44
import time
start = time.time()
stop = 10001
pentagon = { n*(3*n -1)/2 for n in range(1,stop) }

for j in range(1,stop):
    for k in range(j,stop):
        pj = j*(3*j -1)/2 
        pk = k*(3*k -1)/2
        s = pj + pk
        d = pk - pj
        sd = {s,d}
        if len(pentagon & sd) > 1:
            print(pentagon & sd, j,k)
            print(pk - pj)
            print(time.time()-start)
            exit()

# from math import sqrt
# from datetime import datetime
# q = datetime.now()

# def is_pent(n):
#     a = (sqrt(24*n + 1) + 1) / 6
#     return a.is_integer() and a > 0

# pents = {1}
# c = 2
# k = 1
# while True:
#     for i in pents:
#         if k - i in pents and is_pent(k+i):
#             print(datetime.now() - q)
#             print(k-i)
#             quit()
#     pents.add(k)
#     k += 3*c - 2
#     c += 1