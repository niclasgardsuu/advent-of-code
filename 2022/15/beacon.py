with open("input.txt",'r') as f:
    data = f.read()
data = data.split('\n')

beacons = []
sensors = []
for i, row in enumerate(data):
    row = row.replace('x=','').replace('y=','').replace(',','').replace(':','')
    row = row.split()
    x1 = int(row[2])
    y1 = int(row[3])
    x2 = int(row[8])
    y2 = int(row[9])

    sensors.append([x1,y1])
    beacons.append([x2,y2])

check = 2000000

dists = dict()
covers = []
for i in range(len(sensors)):
    dist = abs(sensors[i][0] - beacons[i][0]) + abs(sensors[i][1] - beacons[i][1])
    dists[i] = dist

    if beacons[i][1] == check:
        if sensors[i][0] > beacons[i][0]:
            covers.append([beacons[i][0] + 1, 2*sensors[i][0] - beacons[i][0]])
        elif sensors[i][0] < beacons[i][0]:
            covers.append([2*sensors[i][0] - beacons[i][0], beacons[i][0] - 1])
        continue

    if sensors[i][1] < check:
        if sensors[i][1] + dist > check :
            dist = dist - (check - sensors[i][1])
            covers.append([sensors[i][0] - dist, sensors[i][0] + dist])
    else:
        if sensors[i][1] - dist < check :
            dist = dist - (sensors[i][1] - check)
            covers.append([sensors[i][0] - dist, sensors[i][0] + dist])

test = set()
for i in range(-400000,5000000):
    for c in covers:
        if i >= c[0] and i <= c[1]:
            test.add(i)
            break
        
_break = False
for i in range(len(sensors)):
    if _break: break
    for j in range(len(sensors)):
        if _break: break
        dsensors = abs(sensors[i][0] - sensors[j][0]) + abs(sensors[i][1] - sensors[j][1])
        if (dists[i] + dists[j] + 2) == dsensors:
            for k in range(len(sensors)):
                if _break: break
                for l in range(len(sensors)):
                    if _break: break
                    dsensors2 = abs(sensors[k][0] - sensors[l][0]) + abs(sensors[k][1] - sensors[l][1])
                    if (dists[k] + dists[l] + 2) == dsensors2 and k != i and k != j and l != i and l != j:
                        print(i,j,k,l)
                        _break = True
                        break
                        #sorry bad solution sorry sorry
#magic
diagonal3124 = set()
y = sensors[31][1] + dists[31] + 1
for x in range(sensors[31][0], sensors[24][0]):
    diagonal3124.add((x,y))
    y -= 1
diagonal629 = set()
y = sensors[6][1] - dists[6] - 1
for x in range(sensors[6][0], sensors[29][0]):
    diagonal629.add((x,y))
    y += 1

for c in diagonal629:
    if c in diagonal3124:
        print(c[0], "*", c[1], "=", c[0]*4000000 + c[1])
print(len(test))