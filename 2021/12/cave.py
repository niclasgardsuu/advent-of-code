from functools import cache

with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')

paths = dict()
for row in rows:
    path = row.split('-')
    if not path[0] in paths:
        paths[path[0]] = []
    if not path[1] in paths:
        paths[path[1]] = []
    if path[1] != 'start' and path[0] != 'end':
        paths[path[0]].append(path[1])
    if path[1] != 'end'   and path[0] != 'start':
        paths[path[1]].append(path[0])

taken = dict()
for node in paths:
    taken[node] = 0

def depth_first(node):
    if node == 'end':
        return [[node]]
    if node.islower():
        taken[node] += 1
    current_paths = []
    for neighbor in paths[node]:
        how_many_2s = sum([1 if taken[node] >= 2 and node.islower() else 0 for node in paths])
        if taken[node] <= 2 and how_many_2s <= 1:
            cont_paths = depth_first(neighbor)
        else:
            continue
        for cont_path in cont_paths:
            current_paths.append([node] + cont_path)
    taken[node] -= 1
    return current_paths

a = depth_first('start')
print(len(a))