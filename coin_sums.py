# Problem 31
# In England the currency is made up of pound, £, and pence, p, and there are 
# eight coins in general circulation:
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
# It is possible to make £2 in the following way:
# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?

coins = [1, 2, 5, 10, 20, 50, 100, 200]
amount = 2000
already_learned_ways = {}

def ways_to_make(target,avc):
    global coins
    global already_learned_ways
    if avc <= 0:
        return 1
    t = target
    if f"{t}:{avc}" in already_learned_ways:
        return already_learned_ways[f"{t}:{avc}"]
    res = 0
    while target >= 0:
        res += ways_to_make(target, avc-1)
        target -= coins[avc]
    already_learned_ways[f"{t}:{avc}"] = res
    return res

print(ways_to_make(amount,len(coins)-1))