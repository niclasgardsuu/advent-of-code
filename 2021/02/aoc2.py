with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')
instructions = []
for row in rows:
    instructions.append(row.split(' '))

depth = 0
pos = 0
aim = 0

for inst in instructions:
    if(inst[0] == 'up'):
        aim -= int(inst[1])
    elif(inst[0] == 'down'):
        aim += int(inst[1])
    elif(inst[0] == 'forward'):
        depth += aim*int(inst[1])
        pos += int(inst[1])

print("depth: " + str(depth))
print("pos:   " + str(pos))
print(pos*depth)