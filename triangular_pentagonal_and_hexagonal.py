# Problem 45

rang = 100_000
pentagonal = {(n*(3*n - 1)/2) for n in range(rang)}
hexagonal = {(n*(2*n - 1)) for n in range(rang)}

print(pentagonal & hexagonal)