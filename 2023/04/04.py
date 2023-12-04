import time
with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')

tic = time.time()

p1 = 0
card_matches = dict()
for i, row in enumerate(rows):
    card_num = i
    win, have = row[8:].split(' | ')
    points = 1
    matches = 0
    for num in win.split():
        if num in have.split():
            points*=2
            matches += 1
    p1+=points//2
    card_matches[card_num] = matches

from functools import cache
@cache
def how_many_cards(card):
    sum = 1
    for i in range(card_matches[card]):
        sum += how_many_cards(card+i+1)
    return sum


print(p1)
print(sum(map(how_many_cards,range(len(rows)))))

toc = time.time()
print(f'{toc-tic:2f} sec')