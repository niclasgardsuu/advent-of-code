with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')
elves = [[]]
for row in rows:
    if len(row) > 0:
        elves[-1].append(int(row))
    else:
        elves.append([])
sums = [sum(elf) for elf in elves]
sums.sort(reverse=True)
result1 = sums[0]
result2 = sum(sums[0:3])
print(result1)
print(result2)