with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')
for i in range(len(rows)):
    rows[i] = rows[i] + '.'

num_start_pos = []
for y, row in enumerate(rows):
    prev_not_digit = True
    for x, value in enumerate(row):        
        if value.isdigit() and prev_not_digit:
            num_start_pos.append((x,y))
            prev_not_digit = False
        elif value.isdigit():
            continue   
        else:
            prev_not_digit = True

def has_adjacent_symbol(rows, num_pos, num_length):
    has_adjacent = False
    start_window = (num_pos[0]-1,num_pos[1]-1) 
    stop_window = (num_pos[0] + num_length + 1, num_pos[1]+1+1)
    
    if start_window[0] < 0:
        start_window = (0,start_window[1])
    if start_window[1] < 0:
        start_window = (start_window[0],0)
    if stop_window[0] >= len(rows[0]):
        stop_window = (len(rows[0]),stop_window[1])
    if stop_window[1] >= len(rows):
        stop_window = (stop_window[0],len(rows))

    dots = 0
    for y in range(start_window[1], stop_window[1]):
        for x in range(start_window[0], stop_window[0]):
            if rows[y][x] == '.':
                dots += 1

    if dots != (start_window[0]-stop_window[0])*(start_window[1]-stop_window[1]) - num_length:
        return True
    else:
        return False

def add_adjacent_gears(rows, num_pos, num_length, gear_to_num):
    has_adjacent = False
    start_window = (num_pos[0]-1,num_pos[1]-1) 
    stop_window = (num_pos[0] + num_length+1, num_pos[1]+2)
    
    if start_window[0] < 0:
        start_window = (0,start_window[1])
    if start_window[1] < 0:
        start_window = (start_window[0],0)
    if stop_window[0] >= len(rows[0]):
        stop_window = (len(rows[0]),stop_window[1])
    if stop_window[1] >= len(rows):
        stop_window = (stop_window[0],len(rows))

    dots = 0
    for y in range(start_window[1], stop_window[1]):
        for x in range(start_window[0], stop_window[0]):
            if rows[y][x] == '*':
                if (x,y) in gear_to_num:
                    gear_to_num[(x,y)].append(num_pos)
                else:
                    gear_to_num[(x,y)] = [num_pos]
                return True
    return False

def calc_num(rows, num_pos, num_length):
    return int(''.join(rows[num_pos[1]][num_pos[0]:num_pos[0]+num_length]))

part1 = 0
num_lengths = dict()
for num in num_start_pos:
    num_length = 0
    while rows[num[1]][num[0] + num_length].isdigit():
        num_length += 1
    num_lengths[num] = num_length
    if has_adjacent_symbol(rows,num,num_length):
        part1 += int(''.join(rows[num[1]][num[0]:num[0]+num_length]))

part2 = 0
gear_to_num = dict()
for num in num_start_pos:
    add_adjacent_gears(rows,num,num_lengths[num], gear_to_num)

for gear, nums in gear_to_num.items():
    if len(nums) == 2:
        part2 += calc_num(rows,nums[0],num_lengths[nums[0]]) * calc_num(rows,nums[1],num_lengths[nums[1]])

print(part1)
print(part2)