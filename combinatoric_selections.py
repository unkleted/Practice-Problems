# Problem 53
from math_stuff import factorial
total = 0
for n in range(23,101):
    for r in range(1,n+1):
        nr = factorial(n) / (factorial(r) * factorial(n-r))
        if nr > 1_000_000:
            total += 1
print(total)