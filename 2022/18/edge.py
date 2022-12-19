with open('input.txt','r') as f:
    data = f.read()
rocks = data.split('\n')
rocks = list(map(lambda x: tuple(list(map(int,x.split(',')))),rocks))

def count_edges(rocks):
    rock_set = set()
    edges = 0
    for rock in rocks:
        rock_set.add(rock)
        edges += 6
        if (rock[0] - 1, rock[1], rock[2]) in rock_set:
            edges -= 2
        if (rock[0] + 1, rock[1], rock[2]) in rock_set:
            edges -= 2
        if (rock[0], rock[1]- 1, rock[2]) in rock_set:
            edges -= 2
        if (rock[0], rock[1] + 1, rock[2]) in rock_set:
            edges -= 2
        if (rock[0], rock[1], rock[2] - 1) in rock_set:
            edges -= 2
        if (rock[0], rock[1], rock[2] + 1) in rock_set:
            edges -= 2
    return edges
print(count_edges(rocks))

# Assuming 10,10,10 is in the middle of the hole, and that there is only one hole
# yea i know, its bad

def check(rock, set, new_set):
    return rock not in set and rock not in new_set


visited = set()
queue = [(0,0,0)] # starting position of breadth first
while len(queue) > 0:
    rock = queue.pop()
    visited.add(rock)

    next1 = (rock[0] - 1, rock[1], rock[2])
    next2 = (rock[0] + 1, rock[1], rock[2])
    next3 = (rock[0], rock[1] - 1, rock[2])
    next4 = (rock[0], rock[1] + 1, rock[2])
    next5 = (rock[0], rock[1], rock[2] - 1)
    next6 = (rock[0], rock[1], rock[2] + 1)

    if next1 not in visited and next1 not in rocks and next1[0] >= -1:
        queue.append(next1)
    if next2 not in visited and next2 not in rocks and next2[0] <= 22:
        queue.append(next2)
    if next3 not in visited and next3 not in rocks and next3[1] >= -1:
        queue.append(next3)
    if next4 not in visited and next4 not in rocks and next4[1] <= 22:
        queue.append(next4)
    if next5 not in visited and next5 not in rocks and next5[2] >= -1:
        queue.append(next5)
    if next6 not in visited and next6 not in rocks and next6[2] <= 22:
        queue.append(next6)

print(len(visited))
print(count_edges(list(visited)) - ((24**2) * 6))
