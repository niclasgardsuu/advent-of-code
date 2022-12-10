import numpy as np
with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')

trees = []
for row in rows:
    trees.append([])
    for tree in row:
        trees[-1].append(int(tree))

trees = np.array(list(map(lambda x: np.array(x), trees)))

count = 0
score = 0
for y in range(1,len(trees)-1):
    for x in range(1,len(trees[0])-1):
        h = trees[y][x]
        s1, s2, s3, s4 = 0,0,0,0
        for t in reversed(trees[y,:x]):
            if t < h:
                s1 += 1
            else:
                break
        for t in trees[y,x+1:]:
            if t < h:
                s2 += 1
            else:
                s2 +=1
                break
        for t in reversed(trees[:y,x]):
            if t < h:
                s3 += 1
            else:
                s3 += 1
                break
        for t in trees[y+1:,x]:
            if t < h:
                s4 += 1
            else:
                s4 += 1
                break

        new = s1*s2*s3*s4
        if new > score:
            score = new
        
        check = any(h <= t for t in trees[y,:x]) and any(h <= t for t in trees[y,x+1:]) and any(h <= t for t in trees[:y,x]) and any(h <= t for t in trees[y+1:,x])
        if not check:
            count += 1
count += len(trees)*4 - 4

print(score)
print(count)
