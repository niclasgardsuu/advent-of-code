with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')

def split_at(list, split_item):
    for y, item in enumerate(list):
        if item == split_item:
            return [list[:y],list[y+1:]]

def get_instruction(input):
    inst = input.split(' ')
    return [int(inst[1]), int(inst[3]), int(inst[5])]

rows = split_at(rows,'')

board_str = rows[0]
inputs = rows[1]

board = []
for x in range(int(board_str[-1][-2])):
    board.append([])
    for y in reversed(range(len(board_str)-1)):
        char = board_str[y][x*4 + 1]
        if char != ' ':
            board[x].append(char)   

for input in inputs:
    [count, from_, dest] = get_instruction(input)
    for i in range(count):
        board[dest-1].append(board[from_-1].pop())

res = ''
for b in board:
    res = res + b[-1]

print(res)