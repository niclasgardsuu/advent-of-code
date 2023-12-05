import time
with open("input.txt",'r') as f:
    data = f.read()
rowss = data.split('\n\n')

seeds = rowss[0]
rowss = rowss[1:]

maps = [dict() for _ in range(7)]
map_ranges = [dict() for _ in range(7)]

for i, rows in enumerate(rowss):
    for row in rows.split('\n')[1:]:
        dest, soil, range_ = row.split()
        maps[i][int(soil)] = int(dest)  
        map_ranges[i][int(soil)] = int(range_)

locs = []
seeds = seeds.split()[1:]
for seed in seeds:
    curr = int(seed)
    for i in range(7):
        try:
            _key = list(filter(lambda x: curr > x,maps[i].keys()))
            _key.sort(reverse=False)
            _key = _key[-1]
            offset = curr-_key
            _range = map_ranges[i][_key]
            if curr < _key + _range:
                curr = maps[i][_key] + offset
        except: 
            curr = curr
    locs.append(int(curr))
print(min(locs))

##################################### PART 2 ############################################
seeds = list(map(int,seeds))
key_ranges = list(zip(seeds[::2],seeds[1::2]))
key_ranges = list(map(lambda x: (x[0], x[0]+x[1]-1), key_ranges))
map_split_points = []
for i in range(7):
    map_split_points.append([])
    for map_key, map_range in map_ranges[i].items():
        map_split_points[-1].append(map_key)
        map_split_points[-1].append(map_key+map_range)
next_key_ranges = []
for i in range(7):
    didnt_split = False
    while not didnt_split:
        didnt_split = True
        for key_start, key_end in key_ranges:
            for split_point in map_split_points[i]:
                if split_point > key_start and split_point <= key_end:
                    next_key_ranges.append((key_start,split_point-1))
                    next_key_ranges.append((split_point,key_end))
                    didnt_split = False
                    break
            else:
                next_key_ranges.append((key_start,key_end))
        key_ranges = next_key_ranges
        next_key_ranges = []
    def new_key(key):
        new = key[0]
        try:
            _key = list(filter(lambda x: key[0] >= x,maps[i].keys()))
            _key.sort(reverse=False)
            _key = _key[-1]
            offset = key[0]-_key
            _range = map_ranges[i][_key]
            if key[0] < _key + _range:
                new = maps[i][_key] + offset
        except: 
            miss = True
        return (new, key[1]- (key[0]-new))
    key_ranges = list(map(new_key,key_ranges))

print(min(key_ranges,key = lambda x: x[0])[0])