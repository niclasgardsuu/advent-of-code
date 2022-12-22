with open('input.txt') as f:
    data = f.read()
rows = data.split('\n')
monkeys = dict()
for i, row in enumerate(rows):
    name = row.replace(':','').split()[0]
    monkeys[name] = i

def calculate(monkey):
    row = monkeys[monkey]
    current = rows[row].split()
    if len(current) == 2:
        return int(current[1])
    else:
        if current[2] == '+':
            return calculate(current[1]) + calculate(current[3])
        elif current[2] == '-':
            return calculate(current[1]) - calculate(current[3])
        elif current[2] == '*':
            return calculate(current[1]) * calculate(current[3])
        elif current[2] == '/':
            return calculate(current[1]) / calculate(current[3])

print("          root:",int(calculate('root')))

def get_root_branches():
    return rows[monkeys['root']].split()[1:4:2]

def edit_human(diff):
    rows[monkeys['humn']] = "humn: " + str(int(rows[monkeys['humn']].split()[-1])+diff)


print("before | ",rows[monkeys['humn']])

eq = get_root_branches() # get a handle to the two branches that should be equal

#vilket håll ska vi?
diff = calculate(eq[0]) - calculate(eq[1])
edit_human(1)
if (calculate(eq[0]) - calculate(eq[1])) < abs(diff):
    dir = 10000000000000 # diff är mindre efter vi ökat, alltså ska vi fortsätta öka för o komma närmre
else:
    dir = -10000000000000 #annars sänk

equals = False
while not equals:
    pre_diff = diff
    diff = calculate(eq[0]) - calculate(eq[1]) 
    if diff == 0:
        equals = True
    else:
        # om vi ökat så pass mycke så vi gått förbi värdet vi letar efter, byt riktning och gå långsammare mot talet vi letar efter
        if (pre_diff > 0 and diff < 0) or (pre_diff < 0 and diff > 0):
            dir = (-1*dir) // 2 ## dehär gör så att precondition är att talet vi letar efter är en int
        edit_human(dir)

print("after  | ", rows[monkeys['humn']])
