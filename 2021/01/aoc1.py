with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')
array = []
for row in rows:
    array.append(int(row))

count = 0
for n in range(len(array)-1):
    if(array[n+1] > array[n]):
        count = count + 1
print(count)

count2 = 0
for n in range(len(array)-3):
    if(array[n] < array[n+3]):
        count2 = count2 + 1
print(count2)
