# Problem 56

max_s = 0
for a in range(1,100):
    for b in range(1,100):
        c = a**b
        s = 0
        for d in str(c):
            s += int(d)
        if s > max_s:
            max_s = s
print(max_s)