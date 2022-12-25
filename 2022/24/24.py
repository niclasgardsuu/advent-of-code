with open('input.txt') as f:
    data = f.read()
rows = data.split('\n')

right = [[False for _ in range(len(rows[0]))] for _ in range(len(rows))]
down = [[False for _ in range(len(rows[0]))] for _ in range(len(rows))]
left = [[False for _ in range(len(rows[0]))] for _ in range(len(rows))]
up = [[False for _ in range(len(rows[0]))] for _ in range(len(rows))]

# Add borders as constant blizzards, meaning we cant move there
for y in range(len(rows)):
    right[y][0] = True
    down[y][0] = True
    left[y][0] = True
    up[y][0] = True
    right[y][len(rows[0])-1] = True
    down[y][len(rows[0])-1] = True
    left[y][len(rows[0])-1] = True
    up[y][len(rows[0])-1] = True
for x in range(len(rows[0])):
    right[0][x] = True
    down[0][x] = True
    left[0][x] = True
    up[0][x] = True
    right[len(rows)-1][x] = True
    down[len(rows)-1][x] = True
    left[len(rows)-1][x] = True
    up[len(rows)-1][x] = True

# remove constant blizzards in start and end tiles
right[0][1] = False
down[0][1] = False
left[0][1] = False
up[0][1] = False
right[len(rows)-1][len(rows[0])-2] = False
down[len(rows)-1][len(rows[0])-2] = False
left[len(rows)-1][len(rows[0])-2] = False
up[len(rows)-1][len(rows[0])-2] = False
for y in range(1,len(rows)-1):
    for x in range(1,len(rows[0])-1):
        if rows[y][x] == '>':
            right[y][x] = True
        if rows[y][x] == 'v':
            down[y][x] = True
        if rows[y][x] == '<':
            left[y][x] = True
        if rows[y][x] == '^':
            up[y][x] = True

def blizz(right, down, left, up):
    for row in right[1:-1]:
        row.insert(1,row.pop(len(row)-2))
    down.insert(1,down.pop(len(down)-2))
    for row in left[1:-1]:
        row.insert(len(row)-2,row.pop(1))
    up.insert(len(up)-2,up.pop(1))

def get_blizzards(x, y, right, down, left, up):
    if y < 0 or y > len(up)-1: #should be the only coordingate to ever be able to be called negatively
        return [True, True, True, True]

    return [right[y][x], down[y][x], left[y][x], up[y][x]]

def move_from_start_to_dest(start, dest):
    queue = [start]
    moves = 0
    found = False
    while not found:
        #move blizzards
        blizz(right, down, left, up)

        #add next possible positions
        next_queue = queue.copy()
        for x, y in queue:
            if any(get_blizzards(x,y, right, down, left, up)):
                next_queue.remove((x,y))
            if not any(get_blizzards(x+1,y, right, down, left, up)):
                next_queue.append((x+1,y))
            if not any(get_blizzards(x,y+1, right, down, left, up)):
                next_queue.append((x,y+1))
            if not any(get_blizzards(x-1,y, right, down, left, up)):
                next_queue.append((x-1,y))
            if not any(get_blizzards(x,y-1, right, down, left, up)):
                next_queue.append((x,y-1))
        moves += 1

        #remove duplicates and update queue
        queue = list(set(next_queue))

        if dest in queue:
            found = True

    return moves
first = move_from_start_to_dest((1,0), (len(rows[0])-2, len(rows)-1))
second = move_from_start_to_dest((len(rows[0])-2, len(rows)-1), (1,0))
third = move_from_start_to_dest((1,0), (len(rows[0])-2, len(rows)-1))
print(first + second + third)