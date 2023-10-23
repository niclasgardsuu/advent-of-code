with open("input.txt",'r') as f:
    data = f.read()
rows = [[int(v) for v in row] for row in data.split('\n')]

def to_str(list):
    return [str(v) for v in list]

done = False
iteration = 0
flashes_part1 = 0
while True:
    flashed = [[False for _ in range(len(rows[0]))] for _ in range(len(rows))]
    flashes_part2 = flashes_part1
    # Increase energy level
    for y in range(len(rows)):
        for x in range(len(rows[0])):
            rows[y][x] += 1
    
    def flash(x,y):
        if rows[y][x] <= 9:
            return 0 # Don't flash
        
        rows[y][x] = 0
        flashed[y][x] = True
        fs = 0
        # Flash adjacent octopi(uses?)
        for dy in range(-1,2):
            for dx in range(-1,2):
                if x+dx < 0 or x+dx > 9 or y+dy < 0 or y+dy > 9:
                    continue # Outside grid
                if not flashed[y+dy][x+dx]: # Don't get flashed again
                    rows[y+dy][x+dx] += 1
                    fs += flash(x+dx,y+dy)
        return 1 + fs

    # Flash check
    for y, row in enumerate(rows):
        for x, v in enumerate(row):
            flashes_part1 += flash(x,y)

    iteration+=1
    flashes_part2 = flashes_part1 - flashes_part2
    if iteration == 100:
        print('part1:',flashes_part1)
    if flashes_part2 == 100:
        break

print('part2:',iteration)