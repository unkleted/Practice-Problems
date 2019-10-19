# Problem 40

d = '.'
i = 1
# Create the irrational decimal by concatenating the positive integers
while len(d) < 1_000_001:
    d += str(i)
    i += 1
product = 1
# find the 1, 10, 100, 1000, 10000, 100000, and 1000000 digit.
for t in range(7):
    product *= int((d[10**t]))
print(product)