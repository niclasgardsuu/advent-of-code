from functools import cache

with open('input.txt') as f:
    data = f.read()
blueprints = data.split('\n')

def make_blueprint(b):
    blueprint = []
    parse = b.split()
    blueprint.append([int(parse[6]),0,0])
    blueprint.append([int(parse[12]),0,0])
    blueprint.append([int(parse[18]),int(parse[21]),0])
    blueprint.append([int(parse[27]),0,int(parse[30])])
    print(blueprint)
    return blueprint

blueprints = list(map(make_blueprint,blueprints))
blueprints = blueprints[:3]
print(blueprints)
@cache
def geodes(r, c_r, o_r, g_r, time, ore, clay, obsidian):
    if time == 0:
        return 0
    possible = []

    more_ore = 0 if ore >= max_r*time else r 
    more_clay = 0 if clay >= max_c_r*time else c_r
    more_obsidian = 0 if ore >= max_o_r*time else o_r

    #köp robot
    if ore >= blueprint[0][0] and r < max_r:
        possible += [geodes(r+1,c_r,o_r,g_r,time-1,ore+more_ore-blueprint[0][0],clay+more_clay,obsidian+more_obsidian)]
    if ore >= blueprint[1][0] and c_r < max_c_r:
        possible += [geodes(r,c_r+1,o_r,g_r,time-1,ore+more_ore-blueprint[1][0],clay+more_clay,obsidian+more_obsidian)]
    if ore >= blueprint[2][0] and clay >= blueprint[2][1] and o_r < max_o_r:
        possible += [geodes(r,c_r,o_r+1,g_r,time-1,ore+more_ore-blueprint[2][0],clay+more_clay-blueprint[2][1],obsidian+more_obsidian)]
    if ore >= blueprint[3][0] and obsidian >= blueprint[3][2]:
        possible += [geodes(r,c_r,o_r,g_r+1,time-1,ore+more_ore-blueprint[3][0],clay+more_clay,obsidian+more_obsidian-blueprint[3][2])]
    #köp inte nån
    if r != max_r or c_r != max_c_r or o_r != max_o_r:
        possible += [geodes(r,c_r,o_r,g_r,time-1,ore+more_ore,clay+more_clay,obsidian+more_obsidian)]

    return g_r + max(possible)

sum = 0
prod = 1
for i in range(len(blueprints)):
    blueprint = blueprints[i]
    max_r = max([cost[0] for cost in blueprint])
    max_c_r = max([cost[1] for cost in blueprint])
    max_o_r = max([cost[2] for cost in blueprint])
    result = geodes(1,0,0,0,24,0,0,0) * (i+1)
    sum += result
    print(geodes.cache_info())
    geodes.cache_clear()
    print(result)
    # result2 = geodes(1,0,0,0,32,0,0,0) * (i+1)
    # prod *= result2
    # geodes.cache_clear()
    # print(result2)
    print("------")
print("part1: ", sum)
print("part2: ", prod)
