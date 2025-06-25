from time import time
import sys

sys.setrecursionlimit(1000000000)
sys.set_int_max_str_digits(100000000)

def time_factorial(a):
    def factorial(a):
        if a == 0: return 1
        if a == 1: return 1
        return factorial(a-1) * a
    time1 = time()
    fact = factorial(a)
    fact
    time2 = time()
    return time2 - time1

def factorial(a):
    if a == 0: return 1
    if a == 1: return 1
    return factorial(a-1) * a


print(time_factorial(99999))

test_fac = factorial(99999)
print(len(str(test_fac)))