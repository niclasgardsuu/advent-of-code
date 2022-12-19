from functools import cache

with open('input.txt','r') as f:
    data = f.read()
nodes = data.split('\n')
cave = dict()
pressure = dict()
for node in nodes:
    label = node.split()[1]
    neighbors = node.replace(',','').split()[9:]
    print(label, "-", neighbors)
    cave[label] = set()
    for neighbor in neighbors:
        cave[label].add(neighbor)
    pressure[label] = int(node.replace('rate=','').replace(';','').split()[4])

opt_visit = ()
total = 0
@cache
def get_most_pressure(current, time, opened, elephant):
    
    if time == 0 and not elephant:
        return get_most_pressure('AA',26,opened,True)
    elif time == 0:
        return 0
    
    next = [get_most_pressure(neighbor,time-1,opened,elephant) for neighbor in cave[current]]
    open_valve = []
    if current not in opened and pressure[current] > 0:
        opened = tuple(sorted([*opened, current]))
        open_valve = [get_most_pressure(current,time-1,opened,elephant) + (time-1)*pressure[current]]


    return max(next + open_valve)

print(get_most_pressure('AA', 26, (), False))
