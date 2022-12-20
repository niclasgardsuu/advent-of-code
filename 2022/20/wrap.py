with open('input.txt') as f:
    data = f.read()
ns = list(map(int,data.split('\n')))

def index_ints(l):
    res = []
    for i in range(len(l)):
        res.append((i,l[i]))
    return res

def index_ints_part2(l):
    res = []
    for i in range(len(l)):
        a = i
        b = (l[i]*811589153)%(len(l)-1)
        c = (l[i]*811589153)//(len(l)-1)
        res.append((a,b,c))
    return res

def overlap(l, rev = False):
    res = []
    for i in range(len(l)-1):
        res.append(l[i:i+2] if not rev else list(reversed(l[i:i+2])))
    return list(res) if not rev else list(reversed(list(res)))

def find_index(l, index):
    for i in range(len(l)):
        if l[i][0] == index:
            return i
    return -1

def find_value(l, value):
    for i in range(len(l)):
        if l[i][1] == value:
            return i
    return -1

def p(numbers):
    s = ''
    for _, n in numbers:
        s += str(n).rjust(3) + '|'
    print(s)

numbers = index_ints(ns)
for i in range(len(numbers)):
    f = find_index(numbers, i)
    t = (f + numbers[f][1]) % (len(numbers) - 1)
    if f < t:
        if numbers[f][1] < 0:
            t += 1
        else:
            t += 1
    else:
        if t == 0:
            t = len(numbers)
        else:
            if numbers[f][1] > 0:
                f += 1
    arr = overlap(range(*tuple(sorted([f, t]))),rev = t < f)
    for fr, to in arr:
        # print(numbers)
        tmp = numbers[fr]
        numbers[fr] = numbers[to]
        numbers[to] = tmp
    # p(numbers)

numbers2 = index_ints_part2(ns)
for _ in range(10):
    for i in range(len(numbers2)):
        f = find_index(numbers2, i)
        t = (f + numbers2[f][1]) % (len(numbers2) - 1)
        if f < t:
            if numbers2[f][1] < 0:
                t += 1
            else:
                t += 1
        else:
            if t == 0:
                t = len(numbers2)
            else:
                if numbers2[f][1] > 0:
                    f += 1
        arr = overlap(range(*tuple(sorted([f, t]))),rev = t < f)
        for fr, to in arr:
            tmp = numbers2[fr]
            numbers2[fr] = numbers2[to]
            numbers2[to] = tmp
    


ii = find_value(numbers, 0)
a = numbers[(ii+1000)%len(numbers)][1]
b = numbers[(ii+2000)%len(numbers)][1]
c = numbers[(ii+3000)%len(numbers)][1]
print(a, "+", b, "+", c, "=", a+b+c)
ii = find_value(numbers2, 0)
a = numbers2[(ii+1000)%len(numbers2)]
b = numbers2[(ii+2000)%len(numbers2)]
c = numbers2[(ii+3000)%len(numbers2)]
a = a[1] + a[2]*(len(numbers2)-1)
b = b[1] + b[2]*(len(numbers2)-1)
c = c[1] + c[2]*(len(numbers2)-1)
print(a, "+", b, "+", c, "=", a+b+c)