with open('input.txt') as f:
    data = f.read()
rows = data.split('\n')

#find max width
width = 0
for row in rows[:-1]:
    if len(row) > width:
        width = len(row)
height = len(rows)-1

#pad rows
for i in range(len(rows)-1):
    padding = ''
    if len(rows[i]) < width:
        padding = 'X'*(width - len(rows[i]))
    rows[i] = 'X' + rows[i].replace(' ','X') + padding + 'X'

#pad columns
rows.insert(0, 'X'*(width + 2))

for row in rows:
    print(row)

board = rows[:-1]

def add_pos(pos, dir):
    if dir == 'u':
        return (pos[0], pos[1] - 1)
    elif dir == 'd':
        return (pos[0], pos[1] + 1)
    elif dir == 'l':
        return (pos[0] - 1, pos[1])
    elif dir == 'r':
        return (pos[0] + 1, pos[1])
    print("ERROR:")
    print("ERROR: INVALID DIRECTION")
    print("ERROR:")
    exit(1)

def find_wrap_pos(pos, dir):
    if dir == 'u':
        for y in reversed(range(1,height+1)):
            if board[y][pos[0]] != 'X':
                return (pos[0], y)
    if dir == 'd':
        for y in range(1,height+1):
            if board[y][pos[0]] != 'X':
                return (pos[0], y)
    if dir == 'l':
        for x in reversed(range(1,width+1)):
            if board[pos[1]][x] != 'X':
                return (x, pos[1])
    if dir == 'r':
        for x in range(1,width+1):
            if board[pos[1]][x] != 'X':
                return (x, pos[1])

    print('ERROR: INVALID DIRECTION')
    exit(1)

def find_next_pos(pos, dir):
    next_pos = add_pos(pos,dir)
    next_tile = board[next_pos[1]][next_pos[0]]
    if next_tile == '#':
        return pos
    if next_tile == 'X':
        next_pos = find_wrap_pos(pos, dir)
        next_tile = board[next_pos[1]][next_pos[0]]
        if next_tile == '#':
            return pos
        else:
            return next_pos
    else:
        return next_pos

def turn(dir, input):
    if input == 'R':
        if dir == 'u':
            return 'r'
        elif dir == 'd':
            return 'l'
        elif dir == 'l':
            return 'u'
        elif dir == 'r':
            return 'd'
    elif input == 'L':
        if dir == 'u':
            return 'l'
        elif dir == 'd':
            return 'r'
        elif dir == 'l':
            return 'd'
        elif dir == 'r':
            return 'u'
    print("ERROR:")
    print("ERROR: invalid direction")
    print("ERROR:")
    exit(1)

def arrow(dir):
    if dir == 'u':
        return '^'
    elif dir == 'd':
        return 'V'
    elif dir == 'l':
        return '<'
    elif dir == 'r':
        return '>'
    print("ERROR:")
    print("ERROR: invalid direction")
    print("ERROR:")
    exit(1)

def draw(pos, s):
            board[pos[1]] = list(board[pos[1]])
            board[pos[1]][pos[0]] = s
            board[pos[1]] = "".join(board[pos[1]])


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
    return arr

path = rows[-1]
pos = (board[1].index('.'), 1)
dir = 'r'
path = split_numbers_and_letters(path)

for input in path[1:]:
    if type(input) == int:
        for _ in range(int(input)):
            draw(pos, arrow(dir))
            pos = find_next_pos(pos,dir)
    else:
        dir = turn(dir, input)

draw(pos,'@')

for row in board:
    print(row)
print(pos, dir, pos[0]*4 + pos[1]*1000 + (0 if dir == 'r' else (1 if dir == 'd' else (2 if dir == 'l' else 3))))