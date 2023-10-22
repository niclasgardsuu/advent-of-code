with open("input.txt",'r') as f:
    data = f.read()
data = data.split('\n\n')
start = data[0]
formulas_list = data[1].split('\n')
formulas = dict()
for formula in formulas_list:
    f = formula.split(' -> ')
    formulas[f[0]] = f[1]

from functools import cache

@cache
def how_many(c, pair, iter):
    if iter > 0:
        if formulas[pair] == c:
            return 1 + how_many(c, pair[0]+c, iter-1) + how_many(c, c+pair[1], iter-1)
        else:
            return     how_many(c, pair[0]+formulas[pair], iter-1) + how_many(c, formulas[pair]+pair[1], iter-1)
    return 0
    
def get_counts(iterations):
    counts = dict()
    for c in set(formulas.values()):
        if not c in counts:
            counts[c] = 0
        for i in range(len(start)-1):
            print(c, start[i:i+2])
            counts[c] += how_many(c,start[i:i+2],iterations)
    for s in start:
        counts[s] += 1
    return counts

for key, value in formulas.items():
    print(f'{key} -> {value}')


counts = list(get_counts(10).values())
counts.sort()
part1 = counts[-1]-counts[0]

counts = list(get_counts(40).values())
counts.sort()
part2 = counts[-1]-counts[0]
print(part1)
print(part2)