with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')
numbers = []
numberslife = []
numbersoxy = []
for row in rows:
    numbers.append(int(row,2))
    numberslife.append(int(row,2))
    numbersoxy.append(int(row,2))

life = 0
oxy = 0
for n in list(reversed(range(len(rows[0])))):
    count = 0
    for num in numberslife:
        if(num & (2**n)):
            count += 1
    if(count >= (len(numberslife)/2)):
        numberslife = list(filter(lambda x: x & 2**n, numberslife))
    else:
        numberslife = list(filter(lambda x: not(x & 2**n), numberslife))
life = numberslife[0]

for n in list(reversed(range(len(rows[0])))):
    count = 0
    for num in numbersoxy:
        if(num & (2**n)):
            count += 1
    print("-----")
    print(count)
    print(len(numbersoxy))
    if(count < len(numbersoxy) and len(numbersoxy) > 1):
        if(count < (len(numbersoxy)/2)):
            numbersoxy = list(filter(lambda x: x & 2**n, numbersoxy))
        else:
            numbersoxy = list(filter(lambda x: not(x & 2**n), numbersoxy))

oxy = numbersoxy[0]

print(life)
print(oxy)
print(life*oxy)