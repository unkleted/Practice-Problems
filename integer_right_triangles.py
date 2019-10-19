# Problem 39
# a + b > c.  a + b + c > 2c.  a + b + c <= 1000.  So 2c <= 1000.  c <= 500
p_sqrs = [i**2 for i in range(1,500)]
hypots = {}
for a in range(len(p_sqrs)):
    for b in range(a,len(p_sqrs)):
        if p_sqrs[a] + p_sqrs[b] in p_sqrs:
            p = p_sqrs[a]**.5 + p_sqrs[b]**.5 + (p_sqrs[a] + p_sqrs[b])**.5
            if p <= 1000:
                if p in hypots:
                    hypots[p] += 1
                else:
                    hypots[p] = 1

print(max(hypots,key=hypots.get))