with open("input.txt",'r') as f:
    data = f.read()
crabs = data.split(',')
crabs = [int(v) for v in crabs]

from functools import cache

@cache
def cost(n):
    c = 0
    for i in range(n):
        c += i
    return c

min_s = 10000000000000000000
for t in range(max(crabs)):
    s = sum(map(lambda x: cost(abs(x-t)+1),crabs))
    if s < min_s:
        min_s = s
print(min_s)