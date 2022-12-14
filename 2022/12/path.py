import os
import time
import random

os.system('color')

with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')

def char_to_value(char):
    if char == 'S':
        return ord('a') - 96
    elif char == 'E':
        return ord('z') - 96
    order = ord(char)
    return order - 96 # ascii of a is 97, which should return 1

_map = list(map(lambda x: list(map(char_to_value, x)), rows))
paths = []
starts = []
for y in range(len(_map)):
    paths.append([])
    for x in range(len(_map[0])):
        if rows[y][x] == 'S':
            og_start = (x,y)
        if rows[y][x] == 'a':
            starts.append((x,y))
        elif rows[y][x] == 'E':
            dest = (x,y)
        node = [False,False,False,False] #NEWS
        if y != 0               and _map[y][x] - _map[y-1][x] > -2:
            node[0] = True
        if x != 0               and _map[y][x] - _map[y][x-1] > -2:
            node[2] = True
        if x <= len(_map[0])-2  and _map[y][x] - _map[y][x+1] > -2:
            node[1] = True
        if y <= len(_map)-2     and _map[y][x] - _map[y+1][x] > -2:
            node[3] = True
        paths[-1].append(node)

def move (x, y):
    print("\033[%d;%dH" % (y, x), end="")

def set_color(c, char):
    return f"\033[{c}m{char}\033[37m"


def day12(part, starts, og_start, paths):
    if part == 1:
        starters = [og_start]
    else:
        starters = starts + [og_start]
        random.shuffle(starters)
    shortest = 100000000
    for start in starters:
        os.system('cls')
        move(1,1)
        for y in range(len(rows)):
            for x in range(len(rows[0])):
                move(x+1,y+1)
                print(set_color(37,rows[y][x]))
        found = False
        cost = dict()
        cost[start] = 0
        next_search = [start]
        while not found:
            search = next_search
            next_search = []
            if len(search) == 0:
                cost[dest] = 1000000000
                break
            for s in search:
                for i in range(4):
                    if paths[s[1]][s[0]][i]:
                        dx = 0
                        dy = 0
                        if i == 0:   #North
                            dy = -1
                        elif i == 1: #East
                            dx = 1
                        elif i == 2: #West
                            dx = -1
                        elif i == 3: #South
                            dy = 1
                        next = (s[0] + dx, s[1] + dy)
                        if next not in cost and next not in next_search:
                            cost[next] = cost[s] + 1
                            next_search.append(next)
            for s in next_search:
                move(s[0]+1,s[1]+1)
                print(set_color(33,rows[s[1]][s[0]]))
            time.sleep(0.001)
            for s in next_search:
                move(s[0]+1,s[1]+1)
                print(set_color(32,rows[s[1]][s[0]]))
            if dest in cost:
                found = True
        if cost[dest] < shortest:
            shortest = cost[dest]
    return shortest

print(day12(1,starts,og_start,paths), day12(2,starts,og_start,paths))