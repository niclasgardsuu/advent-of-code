with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')
numbers = []
for row in rows:
    numbers.append(int(row,2))

gamma = 0
epsilon = 0
for n in range(len(rows[0])):
    count = 0
    for num in numbers:
        if(num & (2**n)):
            count += 1
    if(count > (len(rows)/2)):
        gamma += 2**n
    else:
        epsilon += 2**n

print(gamma)
print(epsilon)
print(gamma*epsilon)