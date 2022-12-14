with open("input.txt",'r') as f:
    data = f.read()
rocks = data.split('\n')

_map = [['.' for _ in range(600)] for _ in range(200)]
largest_y = 0
for rock in rocks:
    rock = rock.split(' -> ')
    for i in range(len(rock)-1):
        c1 = list(map(int,rock[i].split(',')))
        c2 = list(map(int,rock[i+1].split(',')))
        
        if c1[1] > largest_y:
            largest_y = c1[1]
        if c2[1] > largest_y:
            largest_y = c2[1]

        if c1[0] == c2 [0]:
            if c1[1] < c2[1]:
                for y in range(c1[1],c2[1]+1):
                    _map[y][c1[0]-200] = '#'
            else:
                for y in range(c2[1],c1[1]+1):
                    _map[y][c1[0]-200] = '#'
        else:
            if c1[0] < c2[0]:
                for x in range(c1[0],c2[0]+1):
                    _map[c1[1]][x-200] = '#'
            else:
                for x in range(c2[0],c1[0]+1):
                    _map[c1[1]][x-200] = '#'

for x in range(len(_map[0])):
    _map[largest_y+2][x] = '#'

for row in _map:
    s = ''
    for c in row:
        s = s + c
    print(s)

count = 0
in_abyss = False
while not in_abyss:
    sand = [300,0]
    falling = True
    while falling:
        if sand[0] <= 0 or sand[0] >= 599 or sand[1] >= 198:
            print("ree finns inte nån abyss")
            in_abyss = True
            break
        if _map[0][300] == 'o':
            in_abyss = True
            break
        if _map[sand[1]+1][sand[0]] == '.':
            sand[1] += 1
        elif _map[sand[1]+1][sand[0]-1] == '.':
            sand[0] -= 1
            sand[1] += 1
        elif _map[sand[1]+1][sand[0]+1] == '.':
            sand[0] += 1
            sand[1] += 1
        else:
            count += 1
            falling = False
            _map[sand[1]][sand[0]] = 'o'
print("------")

for row in _map:
    s = ''
    for c in row:
        s = s + c
    print(s)

print(count)