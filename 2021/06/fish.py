from functools import cache

@cache
def zero_fish(days):
    if days <= 0:
        return 1
    else:
        return zero_fish(days-7) + zero_fish(days-9)
    
with open("input.txt",'r') as f:
    data = f.read()
fishes = [int(a) for a in data.split(',')]

print(sum(map(lambda x: zero_fish(256-x),fishes)))