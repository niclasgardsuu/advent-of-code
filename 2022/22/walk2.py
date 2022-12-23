with open('input.txt') as f:
    data = f.read()
rows = data.split('\n')
inputs = rows[-1]
rows = rows[:-2]

#find max width
width = 0
for row in rows:
    if len(row) > width:
        width = len(row)
height = len(rows)-1

#pad rows
for i in range(len(rows)):
    padding = ''
    if len(rows[i]) < width:
        padding = 'X'*(width - len(rows[i]))
    rows[i] = rows[i].replace(' ','X') + padding

for row in rows:
    x = 1
    #print(row)

#hardcoded region width
region_width = 50

region_corners = [None, None, None, None, None, None]
counter = 0
for y in range(0, len(rows), region_width):
    for x in range(0, len(rows[0]), region_width):
        if rows[y][x] != 'X':
            region_corners[counter] = (x,y)
            counter += 1

region_direction_to_region = []
region_direction_to_edge = []
for r in range(6):
    region_direction_to_region.append([None, None, None, None]) # Right, Down, Left, Up
    region_direction_to_edge.append([None, None, None, None]) # Right, Down, Left, Up
    #Currently we dont know of any connections, therefore None

def region_from_position(pos, corners, width):
    for region, corner in enumerate(corners):
        if pos[0] >= corner[0] and pos[0] < corner[0]+width and pos[1] >= corner[1] and pos[1] < corner[1]+width:
            return region
    return -1 # outside any region

#immediate connections
for r in range(6):
    x, y = region_corners[r]
    right = (x+region_width, y)
    down = (x,y+region_width)
    left = (x-region_width, y)
    up = (x,y-region_width)
    if right in region_corners:
        adj = region_from_position(right, region_corners, region_width)
        region_direction_to_region[r][0] = adj
        region_direction_to_edge[r][0] = 2
        region_direction_to_edge[adj][2] = 0
    if down in region_corners:
        adj = region_from_position(down, region_corners, region_width)
        region_direction_to_region[r][1] = adj
        region_direction_to_edge[r][1] = 3
        region_direction_to_edge[adj][3] = 1
    if left in region_corners:
        adj = region_from_position(left, region_corners, region_width)
        region_direction_to_region[r][2] = adj
        region_direction_to_edge[r][2] = 0
        region_direction_to_edge[adj][0] = 2
    if up in region_corners:
        adj = region_from_position(up, region_corners, region_width)
        region_direction_to_region[r][3] = adj
        region_direction_to_edge[r][3] = 1
        region_direction_to_edge[adj][1] = 3

for r in range(6):
    print(str(region_direction_to_region[r]).ljust(30), str(region_direction_to_edge[r]).ljust(30))

# connect corners until everything is connected
done = False
while not done:
    for r in reversed(range(6)):
        for dir in range(4):
            if region_direction_to_region[r][dir] == None:
                for turn in [-1, 1]: #check left(-1) and right(1) side to fetch edge
                    next_region = region_direction_to_region[r][(dir+turn)%4]
                    if next_region != None:
                        next_dir = region_direction_to_edge[r][(dir+turn)%4]
                        next_next_region = region_direction_to_region[next_region][(next_dir + turn) % 4]
                        if next_next_region != None: # matching edge found
                            next_next_dir = region_direction_to_edge[next_region][(next_dir + turn) % 4]
                            region_direction_to_region[r][dir] = next_next_region
                            region_direction_to_edge[r][dir] = (next_next_dir + turn) % 4
                            region_direction_to_region[next_next_region][(next_next_dir + turn) % 4] = r
                            region_direction_to_edge[next_next_region][(next_next_dir + turn) % 4] = dir
                            break
                        else:
                            continue
                    else:
                        continue

    #possible connectiong have been done, now check if all of them are done
    done = True
    for r in range(6):
        for dir in range(4):
            if region_direction_to_region[r][dir] == None:
                done = False # not done yet, keep going
                

print("----------")
for r in range(6):
    print(str(region_direction_to_region[r]).ljust(30), str(region_direction_to_edge[r]).ljust(30))

def arrow(dir):
    if dir == 0:
        return '>'
    elif dir == 1:
        return 'V'
    elif dir == 2:
        return '<'
    elif dir == 3:
        return '^'

def draw(rows, pos, s):
            rows[pos[1]] = list(rows[pos[1]])
            rows[pos[1]][pos[0]] = s
            rows[pos[1]] = "".join(rows[pos[1]])

def move(pos, dir, steps):
    if dir == 0:
        return (pos[0] + steps, pos[1])
    if dir == 1:
        return (pos[0], pos[1] + steps)
    if dir == 2:
        return (pos[0] - steps, pos[1])
    if dir == 3:
        return (pos[0], pos[1] - steps)

def tile(rows, pos):
    return rows[pos[1]][pos[0]]

def move_and_rotate_in_region(pos, region_corner, region_width, dir_from, dir_to):
    pos = (pos[0] % region_width, pos[1] % region_width)
    if pos[0] >= region_width or pos[1] >= region_width:
        print("ERROR: INVALID POSITION WHEN GETTING LOCAL POSITION IN REGION")
        exit(1)
    rotations = (dir_from - dir_to) % 4 # this tells how many counter clock-wise rotations needs to be done
    for _ in range(rotations):
        pos = (pos[1], region_width - 1 - pos[0])

    return (pos[0] + region_corner[0], pos[1] + region_corner[1])


def find_next_pos_and_direction(rows, pos, dir):
    next_pos = move(pos, dir, 1)
    current_region = region_from_position(pos, region_corners, region_width)
    possibly_next_region = region_from_position(next_pos, region_corners, region_width)
    if current_region == possibly_next_region:
        if tile(rows,next_pos) == '#':
            return pos, dir
        else:
            return next_pos, dir
    else:
        wrap_pos = move(pos, (dir + 2)%4, region_width-1)
        next_region = region_direction_to_region[current_region][dir]
        next_dir = (region_direction_to_edge[current_region][dir] + 2) % 4 # +2 in order to turn away from the edge that we will be coming out of
        wrap_pos = move_and_rotate_in_region(wrap_pos, region_corners[next_region], region_width, dir, next_dir)
        if tile(rows,wrap_pos) == '#':
            return pos, dir
        else:
            return wrap_pos, next_dir
        
def split_numbers_and_letters(s):
    arr = ['DUMMY']
    i = 0
    while i < len(s):
        if s[i].isnumeric():
            if type(arr[-1]) == int:
                arr[-1] = arr[-1]*10 + int(s[i])
            else:
                arr.append(int(s[i]))
        else:
            arr.append(s[i])
        i += 1
    return arr[1:]

def find_index(list, elements):
    index = len(list)
    for elem in elements:
        if elem in list:
            i = list.index(elem)
            if i < index:
                index = i
    return index

inputs = split_numbers_and_letters(inputs)
pos = (find_index(rows[0], ['.', '#']), 0)
dir = 0
for input in inputs:
    if type(input) == int:
        for _ in range(input):
            draw(rows, pos, arrow(dir))
            pos, dir = find_next_pos_and_direction(rows, pos, dir)
    else:
        if input == 'L':
            dir = (dir - 1) % 4
        elif input == 'R':
            dir = (dir + 1) % 4

for row in rows:
    print(row)

draw(rows, pos,'@')
print((pos[0]+1)*4 + (pos[1]+1)*1000 + dir)