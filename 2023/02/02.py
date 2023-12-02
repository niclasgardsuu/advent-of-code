import re
with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')

def max_cubes(row,color):
    return max(map(int, re.findall(f'(\d*)(?= {color})',row)[::2]))

part1 = 0
part2 = 0
for row in rows:
    game_id = int(row.split()[1].replace(':',''))
    reds = max_cubes(row,'red')
    greens = max_cubes(row,'green')
    blues = max_cubes(row,'blue')

    if reds <= 12 and greens <= 13 and blues <= 14:
        part1 += game_id
    
    part2 += reds * greens * blues

print(part1)
print(part2)