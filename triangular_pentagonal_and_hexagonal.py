# Problem 45

rang = 100_000
triangle = [(n*(n+1)/2) for n in range(rang)]
pentagonal = [(n*(3*n - 1)/2) for n in range(rang)]
hexagonal = [(n*(2*n - 1)) for n in range(rang)]

print(triangle[-1], pentagonal[-1], hexagonal[-1])

for hex in hexagonal:
    if hex in triangle and hex in pentagonal:
        print(hex, '<---')