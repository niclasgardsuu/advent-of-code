import numpy as np

with open('input.txt') as f:
    data = f.read()
rows = data.split('\n')

def map_to_bool(rows):
    res = []
    for row in rows:
        r = []
        for char in row:
            if char == '.':
                r.append(False)
            elif char == '#':
                r.append(True)
        res.append(r)
    return res

rows = map_to_bool(rows)

padding = 2000
# pad edges. 10 possible moves means at least 10 paddings
rows = [[False]*len(rows[0])]*padding + rows + [[False]*len(rows[0])]*padding
for i in range(len(rows)):
    rows[i] = [False]*(padding//2) + rows[i] + [False]*(padding//2)

# convert to numpy array for cool indexing
rows = np.array(list(map(lambda a: np.array(a),rows)))

# # print initial state
# for row in rows:
#     s = ''
#     for char in row:
#         if char:
#             s += '#'
#         else:
#             s += '.'
#     print(s)
# print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")

def check_dir(x,y, rows, dir):
    if dir == 0:
        if y != 0 and x > 0 and x < len(rows[0]): # uppåt
            if not any(rows[y-1,x-1:x+2]):
                return True
        return False
    elif dir == 1:
        if y != len(rows) and x > 0 and x < len(rows[0]): # neråt
            if not any(rows[y+1,x-1:x+2]):
                return True
        return False
    elif dir == 2:    
        if x != 0 and y > 0 and y < len(rows): # vänster
            if not any(rows[y-1:y+2,x-1]):
                return True
        return False
    elif dir == 3:
        if x != len(rows[0]) and y > 0 and y < len(rows): # höger
            if not any(rows[y-1:y+2,x+1]):
                return True
        return False
    print("INVLAID DIRECTION:")
    exit(1)

#get initial x and y of elves
positions = []
for y, row in enumerate(rows):
    for x, cell in enumerate(row):
        if cell:
            positions.append((x,y))

for iter in range(2000):
    # find possible moves
    moves = []
    for x, y in positions:
        if y == 0:
            ymin = y
            ymax = y+2
        elif y == len(rows):
            ymin = y-1
            ymax = y+1
        else:
            ymin = y-1
            ymax = y+2
        if x == 0:
            xmin = x
            xmax = x+2
        elif x == len(rows[0]):
            xmin = x-1
            xmax = x+1
        else:
            xmin = x-1
            xmax = x+2

        s = sum(sum(rows[ymin:ymax,xmin:xmax]))
        if rows[y,x]:
            if s >= 2:
                for e in range(4):
                    if check_dir(x,y,rows,(iter+e)%4):
                        if (iter + e) % 4 == 0:
                            moves.append(((x,y),(x,y-1)))
                        elif (iter + e) % 4 == 1:
                            moves.append(((x,y),(x,y+1)))
                        elif (iter + e) % 4 == 2:
                            moves.append(((x,y),(x-1,y)))
                        elif (iter + e) % 4 == 3:
                            moves.append(((x,y),(x+1,y)))
                        break
                        

    # filter out bad moves
    good_moves = []
    for i in range(len(moves)):
        found_duplicate = False
        for j in range(len(moves)):
            if i != j and moves[i][1] == moves[j][1]:
                found_duplicate = True
                break
        if not found_duplicate:
            good_moves.append(moves[i])
        
    # execute all moves
    for move in good_moves:
        fr = move[0]
        to = move[1]
        rows[fr[1]][fr[0]] = False
        rows[to[1]][to[0]] = True
        positions.remove(fr)
        positions.append(to)
    
    print(iter)
    if len(moves) == 0:
        break

    # print board at each iteration
    # for row in rows:
    #     s = ''
    #     for char in row:
    #         if char:
    #             s += '#'
    #         else:
    #             s += '.'
    #     print(s)
    # print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")

# find smallest and largest x and y
min_x = len(rows[0])
max_x = 0
min_y = len(rows)
max_y = 0
total_elves = 0
empty = 0

for y, row in enumerate(rows):
    for x, cell in enumerate(row):
        if cell:
            total_elves += 1
            if x < min_x:
                min_x = x
            if x > max_x:
                max_x = x
            if y < min_y:
                min_y = y
            if y > max_y:
                max_y = y
        else:
            empty += 1

print((max_x - min_x + 1) * (max_y - min_y + 1) - total_elves) # kommer printa fel om man fortfarande kör me 2000 iterations, måste ändra den till 10 för att denna ska printa rätt