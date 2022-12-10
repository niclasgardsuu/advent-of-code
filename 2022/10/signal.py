with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')

def draw(drawing, x, cycle):
    if abs(x-((cycle-1)%40)) < 2:
        new_drawing = drawing + '#'
    else:
        new_drawing = drawing + '.'

    if (cycle)%40 == 0:
        new_drawing = new_drawing + '\n'

    return new_drawing

total = 0
x = 1
cycle = 0
drawing = ''
for i, row in enumerate(rows):
    if row.startswith('addx'):
        is_end = ''
        if (cycle+1 - 20) % 40 == 0:
            total += x*(cycle+1)
        elif (cycle+2 - 20) % 40 == 0:
            total += x*(cycle+2)
        drawing = draw(drawing,x,cycle+1)
        drawing = draw(drawing,x,cycle+2)
        x += int(row.split()[1])
        cycle += 2
    else:
        if (cycle+1 - 20) % 40 == 0:
            total += x*(cycle+1)
        drawing = draw(drawing,x,cycle+1)
        cycle += 1
print(total)
print(drawing)