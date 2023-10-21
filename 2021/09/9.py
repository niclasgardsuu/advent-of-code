input = 'input' 
with open(input + '.txt','r') as f:
    data = f.read()
rows = [[int(v) for v in row] for row in data.split('\n')]
rows = [[10 for _ in range(len(rows[0]))]] + rows
for i in range(len(rows)):
    rows[i] = [10] + rows[i] + [10]
rows = rows + [[10 for _ in range(len(rows[0]))]]

if input == 'test': # print
    for row in rows:
        s = ''
        for v in row:
            s += str(v).ljust(3)
        print(s)

def adjacent_are_bigger(x,y):
    return rows[y][x+1] > rows[y][x] and rows[y][x-1] > rows[y][x] and rows[y+1][x] > rows[y][x] and rows[y-1][x] > rows[y][x]

part1 = 0
for y in range(1,len(rows)-1):
    for x in range(1,len(rows[0])-1):
        if adjacent_are_bigger(x,y):
            part1 += 1 + rows[y][x]

for i in range(len(rows)):
    rows[i] = list(map(lambda x: x < 9, rows[i]))

if input == 'test': # print
    for row in rows:
        s = ''
        for v in row:
            s += str(v).ljust(6)
        print(s)




def count_basin(x,y):
    if rows[y][x]:
        res = 1
        rows[y][x] = False
        res += count_basin(x,y+1)
        res += count_basin(x,y-1)
        res += count_basin(x+1,y)
        res += count_basin(x-1,y)
        return res
    else:
        return 0
sizes = []
part2 = 1
for y in range(1,len(rows)-1):
    for x in range(1,len(rows[0])-1):
        basin_size = count_basin(x,y)
        if basin_size > 0:
            sizes.append(basin_size)

sizes.sort()
part2 = sizes[-1]*sizes[-2]*sizes[-3]

print(part1)
print(part2)