# Problem 38
# Take the number 192 and multiply it by each of 1, 2, and 3:
# 192 x 1 = 192
# 192 x 2 = 384
# 192 x 3 = 576
# By concatenating each product we get the 1 to 9 pandigital, 192384576. We will 
# call 192384576 the concatenated product of 192 and (1,2,3).

# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 
# 5, giving the pandigital, 918273645, which is the concatenated product of 9 
# and (1,2,3,4,5).

# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the 
# concatenated product of an integer with (1,2,...,n) where n>1 ?

def is_pandigital(number: int) -> bool:
    s = str(number)
    return len(s) == 9 and set(s) == set("123456789")

max_pandigital = 0

for integer in range(1, 10_000): # 2 5-digit numbers concatenated would be too big
    for numbers in range(2,10):  # 10 numbers concatenated would be too big
        products = [integer * _ for _ in range(1, numbers+1)]
        # s_products = [ str(_) for _ in products]
        concat_product = int(''.join(map(str, products)))
        if is_pandigital(concat_product):
            print(integer, numbers, concat_product)
            if concat_product > max_pandigital:
                max_pandigital = concat_product

print(max_pandigital)