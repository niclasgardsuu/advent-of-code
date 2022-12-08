with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')

import random

directory_stack = []
checklist = []
directory_sizes = dict()
debug = 0
for row in rows:
    if row.startswith('$ cd'):
        if row[5:] == '..': 
            temp = directory_stack.pop()
            directory_sizes[directory_stack[-1]] += directory_sizes[temp]
        else:
            if row[5:] in directory_sizes:
                row = row + str(random.randint(0,1000))
            directory_stack.append(row[5:])
            directory_sizes[row[5:]] = 0
    elif row.startswith('$ ls'):
        None
    elif row.startswith('dir'):
        None
    else:
        file_size = int(row.split(' ')[0])
        debug += int(row.split(' ')[0])
        directory_sizes[directory_stack[-1]] += file_size

res = 0
current_closest = 0
for item in directory_sizes:
    v = directory_sizes[item]
    if v <= 100000:
        res += v
    if v > current_closest and v <= 70000000-directory_sizes['/']:
        current_closest = v
print(res)
print(current_closest)
