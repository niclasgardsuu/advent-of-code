with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')

def parse_input(str):
    inst = str.split(' ')
    return (inst[0], int(inst[1]))

def move(head, dir):
    if dir == 'U':
        return [head[0], head[1]+1]
    elif dir == 'D':
        return [head[0], head[1]-1]
    elif dir == 'R':
        return [head[0]+1, head[1]]
    elif dir == 'L':
        return [head[0]-1, head[1]]

def is_adjacent(head,tail):
    return abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1

def move_adjacent(tail, head):
    dx = head[0] - tail[0]
    dy = head[1] - tail[1]
    if abs(dx) > abs(dy):
        x = tail[0] + (1 if dx > 0 else -1)
        y = head[1]
    elif abs(dy) > abs(dx):
        x = head[0]
        y = tail[1] + (1 if dy > 0 else -1)
    else: 
        x = tail[0] + (1 if dx > 0 else -1)
        y = tail[1] + (1 if dy > 0 else -1)
    return [x,y]

rope = []
for i in range(10):
    rope.append([0,0])
visited = dict()
visited2 = dict()
inputs = map(parse_input,rows)
for input in inputs:
    for s in range(input[1]):
        rope[0] = move(rope[0],input[0])
        for r in range(len(rope)-1):
            if not is_adjacent(rope[r],rope[r+1]):
                rope[r+1] = move_adjacent(rope[r+1],rope[r])
        visited[tuple(rope[1])] = True   # store immediate tail
        visited2[tuple(rope[-1])] = True # store 10th tail

print(len(visited))
print(len(visited2))