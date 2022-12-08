with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')
for y, row in enumerate(rows):
    rows[y] = rows[y].split(',')
    rows[y][0] = rows[y][0].split('-')
    rows[y][1] = rows[y][1].split('-')

for pair in rows:
    for time in pair:
        time[0] = int(time[0])
        time[1] = int(time[1])

complete_overlaps_found = 0
partial_overlaps_found = 0
for pair in rows:
    #complete overlaps
    if pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1]:
        print(pair)
        complete_overlaps_found += 1
    elif pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1]:
        print(pair)
        complete_overlaps_found += 1

    #partial overlaps
    if pair[0][1] >= pair[1][0] and pair[0][0] <= pair[1][1]:
        print(pair)
        partial_overlaps_found += 1
    elif pair[1][1] >= pair[0][0] and pair[1][0] <= pair[0][1]:
        print(pair)
        partial_overlaps_found += 1

print(complete_overlaps_found)
print(partial_overlaps_found)