with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')

def split_at(list, split_item):
    for y, item in enumerate(list):
        print(item)
        if item == split_item:
            return [list[:y+1],list[y+1:]]

def get_instruction(input):
    inst = input.split(' ')
    return [int(inst[1]), int(inst[3]), int(inst[5])]

rows = split_at(rows,'')

board_str = rows[0]
inputs = rows[1]

print(board_str)
board = []
for x in range(int(board_str[-2][-2])):
    board.append([])
    for y in reversed(range(len(board_str)-2)):
        char = board_str[y][x*4 + 1]
        if char != ' ':
            board[x].append(char)   

for j, input in enumerate(inputs):
    print(j)
    [count, from_, dest] = get_instruction(input)
    temp = []
    for i in range(count):
        temp.append(board[from_-1].pop())
    
    for i in range(count):
        board[dest-1].append(temp.pop())


res = ''
for b in board:
    res = res + b[-1]

print(res)