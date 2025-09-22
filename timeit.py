# from time import time
# import time
from time import perf_counter


def time_func(func):
    """This function shows the execution time of the function object passed"""
    def wrap_func(*args, **kwargs):
        # t1 = time()
        t1 = perf_counter()
        result = func(*args, **kwargs)
        # t2 = time()
        t2 = perf_counter()
        print(f"Function {func.__name__!r} executed in {(t2-t1):.4f}s")
        return result
    return wrap_func

# @time_func
# def long_time(n):
#     for i in range(n):
#         for j in range(1_000_000):
#             i*j


# long_time(1000)