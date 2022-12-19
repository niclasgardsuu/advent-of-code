with open('input.txt','r') as f:
    data = f.read()

def dir(c):
    if c == '>':
        return 1
    elif c == '<':
        return -1
    else:
        print("INTE EN PIL")
        exit(1)
data = list(map(dir,data))
print(len(data))
print(len(data)*5)

def create_piece(t, height):
    if t == 0: # liggande streck
        return [[n,height + 4] for n in range(2,6)]
    if t == 1: # +
        return [[n, height + 5] for n in range(2,5)] + [[3, height + 4],[3, height + 6]] 
    if t == 2: # _|
        return [[n, height + 4] for n in range(2,5)] + [[4, height + 5],[4, height + 6]] 
    if t == 3: # stående streck
        return [[2, height + n] for n in range(4,8)]
    if t == 4: # kvadrat
        return [[2 ,height+4],[3,height+4],[2,height+5],[3,height+5]]

# checks collision if a piece moves horizontally
def collision_h(board, piece, dir):
    if any([segment[0] <= 0 for segment in piece]) and dir == -1:
        return True
    if any([segment[0] >= 6 for segment in piece]) and dir == 1:
        return True
    if any([board[segment[1]][segment[0] + dir] == '#' for segment in piece]):
        return True
    else:
        return False

#checks collision if a piece falls
def collision_d(board, piece):
    if any([segment[1] <= 0 for segment in piece]):
        return True
    if any([board[segment[1]-1][segment[0]] == '#' for segment in piece]):
        return True
    else:
        return False

def move_h(piece, dir):
    for segment in piece:
        segment[0] += dir

def move_d(piece):
    for segment in piece:
        segment[1] -= 1

def increase(board, height):
    board_height = len(board)
    if (height + 4) > board_height:
        for _ in range(height + 4 - board_height):
            board.append(['.' for _ in range(7)])

def print_board(board, piece, height):
    for y in reversed(range(height - 7, height+7)):
        s = ''
        for x in range(7):
            if [x,y] in piece:
                s += '@'
            else:
                s += board[y][x]
        print(s)

board = [['.' for _ in range(7)] for _ in range(80000)]
height = -1
iteration = 0
first_h = -1
first_p = -1
second_h = -1
second_p = -1
loop_h = -1
loop_p = -1
rest_h = -1
rest_p = -1
for p in range(30000):
    piece = create_piece(p%5,height)
    falling = True
    while falling:
        
        if (iteration + 2) % 50455 == 0:
            print_board(board,piece,height)
            print("_________", height, p-1)
        
        if iteration == 50453:
            first_h = height
            first_p = p+1
        if iteration == 50453 + 50455:
            loop_h = height - first_h
            loop_p = p+1 - first_p
            second_h = height
            second_p = p+1
            rest_p = (1000000000000 - first_p) % loop_p

        dir = data[iteration%len(data)]
        if not collision_h(board, piece, dir):
            move_h(piece, dir)
        if not collision_d(board, piece):
            move_d(piece)
        else:
            falling = False
        iteration += 1
    
    if p == second_p + rest_p:
        rest_h = height - second_h

    
    current_highest = max([segment[1] for segment in piece])
    if current_highest > height:
        height = current_highest
    for segment in piece:
        board[segment[1]][segment[0]] = '#'

loops = (1000000000000 - first_p - rest_p)/loop_p
print(loops)
print(first_h + loop_h*loops + rest_h) 
print(first_p + loop_p*loops + rest_p) 
print(height+1)
    