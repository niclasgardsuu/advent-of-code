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

rope = [[0,0] for _ in range(10)]
visited = set()
visited2 = set()
inputs = map(parse_input,rows)
for input in inputs:
    for s in range(input[1]):
        rope[0] = move(rope[0],input[0])
        for r in range(len(rope)-1):
            if not is_adjacent(rope[r],rope[r+1]):
                rope[r+1] = move_adjacent(rope[r+1],rope[r])
        visited.add(tuple(rope[1]))   # store immediate tail
        visited2.add(tuple(rope[-1])) # store 10th tail

print(len(visited))
print(len(visited2))


n = "yahojarmo"
m = "aadyahcinbyahojarmo2sc"

fp = hash(n)
m_fp = [hash(m[i:i+9] for i in range(len(m)-len(n)))]

n = [3,1,4,1,5,1,2,6,5,9,8,4,9,7,9,2]
m = [2,6]
def f(str):
    return str[0]*10 % 11 + str[1] % 11
fm = f(m)
for i in range(len(n)-len(m)+1):
    fn = f(n[i:i+2])
    if(fm == fn):
        print(fm)
        print(n[i:i+2])
        print("cock")