with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')
max_number = max([int(a) for a in data.replace('-> ','').replace(',',' ').replace('\n',' ').split()])
for i,row in enumerate(rows):
    rows[i] = row.replace('-> ','').replace(',',' ')

vents = []
for row in rows:
    vent = [int(vent_position) for vent_position in row.split()]
    vents.append(((vent[0],vent[1]),(vent[2],vent[3])))

def sort_tuple(tup):
    res = sorted(tup)
    return (res[0], res[1])

def good_range(start,end):
    if start < end:
        return range(start,end+1)
    else:
        return reversed(range(end,start+1))

field = [[0 for _ in range(max_number+1)] for _ in range(max_number+1)]
for ((x1,y1),(x2,y2)) in vents:
    if x1 == x2 or y1 == y2:
        for x in good_range(x1, x2):
            for y in good_range(y1, y2):
                field[y][x] += 1
    else:
        for x, y in zip(good_range(x1, x2), good_range(y1, y2)):
                field[y][x] += 1

sum = 0 
for row in field:
    for value in row:
        if value > 1:
            sum += 1

for row in field:
    print(row)
print(sum)