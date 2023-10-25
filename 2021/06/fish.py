from functools import cache

import sys
sys.setrecursionlimit(100000)
sys.set_int_max_str_digits(100000)

@cache
def zero_fish(days):
    if days <= 0:
        return 1
    else:
        return zero_fish(days-7) + zero_fish(days-9)
    
with open("input.txt",'r') as f:
    data = f.read()
fishes = [int(a) for a in data.split(',')]

import time

tic = time.perf_counter()
p1 = sum(map(lambda x: zero_fish(8-x),fishes))
toc = time.perf_counter()
print(f'Part 1: {toc - tic:0.6f} sec')

zero_fish.cache_clear()

tic = time.perf_counter()
p2 = sum(map(lambda x: zero_fish(256-x),fishes))
toc = time.perf_counter()
print(f'Part 2: {toc - tic:0.6f} sec')

zero_fish.cache_clear()

tic = time.perf_counter()
p1 = sum(map(lambda x: zero_fish(80-x),fishes))
p2 = sum(map(lambda x: zero_fish(256-x),fishes))
toc = time.perf_counter()
print(f'Part 1 & 2: {toc - tic:0.6f} sec')

zero_fish.cache_clear()

# tic = time.perf_counter()
# p3 = 0
# for i in range(1000):
#     p3 += sum(map(lambda x: zero_fish((i+1)*1000-x),fishes))
# toc = time.perf_counter()
# print(f'Part 3: {toc - tic:0.6f} sec')
# # This does finish executing! About ~6 seconds. Pretty cool considering the original time complexity.

print(p1, p2, sep='\n')