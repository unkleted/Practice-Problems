

def coin_sums(target: int, coins: list[int]) -> int:
    """Returns the number ways the target can be reached using the list of
    coins."""
    cache = { 0: 1 }
    for coin in coins:
        for amnt in range(coin, target+1):
            cache.setdefault(amnt, 0)
            if amnt-coin in cache:
                cache[amnt] += cache[amnt-coin]
    return cache[target]


if __name__ == "__main__":
    TARGET = 200
    my_coins = [1, 2, 5, 10, 20, 50, 100, 200]
    # coins = [25, 5]
    print(coin_sums(TARGET, my_coins))
    