from functools import cache
import sys
sys.setrecursionlimit(3000)

with open("input.txt",'r') as f:
    data = f.read()
data = data.split('\n')

rows = [[int(v) for v in row] for row in data]
    
width = len(rows[0])
height = len(rows)

rows[0][0] = 1

max_turns_away = 10

@cache
def depth_first(x,y,turns_away):
    if turns_away > max_turns_away:
        return 1000000
    if x >= width or y >= height or x < 0 or y < 0:
        return 1000000
    if x == width-1 and y == height-1:
        return rows[y][x]
    return rows[y][x] + min(depth_first(x+1, y, turns_away), 
                            depth_first(x, y+1, turns_away), 
                            depth_first(x-1, y, turns_away+1), 
                            depth_first(x, y-1, turns_away+1)) 

@cache
def depth_first2(x,y,turns_away):
    if turns_away > max_turns_away:
        return 1000000
    if x >= width*5 or y >= height*5 or x < 0 or y < 0:
        return 1000000
    cost = (rows[y%height][x%width] + (x // width) + (y // height) - 1) % 9 + 1
    if x == width*5-1 and y == height*5-1:
        return cost
    return cost + min(depth_first2(x+1, y, turns_away), 
                      depth_first2(x, y+1, turns_away), 
                      depth_first2(x-1, y, turns_away+1), 
                      depth_first2(x, y-1, turns_away+1)) 

for i in reversed(range(10)):
    print(depth_first(0,0,i+1) - 1)
    
for i in reversed(range(10)):
    print(depth_first2(0,0,i+1) - 1)