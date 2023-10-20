with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')
    
points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}
points2 = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

closers = {
    '<': '>',
    '(': ')',
    '[': ']',
    '{': '}'
}

openers = '<([{'

p = 0
p2s = []
for row in rows:
    p2 = 0
    corrupt = False
    opened = []
    for d in row:
        if d in openers:
            opened.append(d)
        else:
            if d != closers[opened.pop()]:
                corrupt = True
                p += points[d]

    # Part 2
    for o in reversed(opened):
        p2 *= 5
        p2 += points2[closers[o]]
    if p2 > 0 and not corrupt:
        p2s.append(p2)

p2s.sort()
p2 = p2s[len(p2s)//2]

print('part 1:', p)
print('part 2:', p2)