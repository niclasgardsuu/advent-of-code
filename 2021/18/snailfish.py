with open('input.txt','r') as f:
    data = f.read()
rows = [eval(row) for row in data.split('\n')]
from math import floor, ceil
from binarytree import Node
def treeify(list, node):
    if isinstance(list[1], int):
        node.right = Node(list[1])
    else:
        node.right = Node(-1)
        treeify(list[1], node.right)

    if isinstance(list[0], int):
        node.left = Node(list[0])
    else:
        node.left = Node(-1)
        treeify(list[0], node.left)

def get_digit_positions(number, paths, path):
    if len(path) > 5:
        return
    
    if isinstance(number,int):
        paths.append(path)
    else:
        get_digit_positions(number[0],paths,path+'0')
        get_digit_positions(number[1],paths,path+'1')

def get_exploder_positions(number, paths, path):
    if isinstance(number,int):
        return
    
    if len(path) >= 4:
        paths.append(path)
    else:
        get_exploder_positions(number[0],paths,path+'0')
        get_exploder_positions(number[1],paths,path+'1')
        
def to_digits(l):
    return [int(i) for i in l]

def get_numbers_from_exploder(number,path):
    curr = number
    for p in to_digits(path):
        curr = curr[p]
    return curr[0], curr[1]

def remove_exploder(number,path):
    curr = number
    for p in to_digits(path[:-1]):
        curr = curr[p]
    curr[int(path[-1])] = 0

def add_to_digit(number,path,value):
    curr = number
    for p in to_digits(path[:-1]):
        curr = curr[p]
    curr[int(path[-1])] += value

    
def get_splitter_positions(number, paths, path):
    if len(path) > 10:
        return
    
    if isinstance(number,int):
        if number > 9:
            paths.append(path)
    else:
        get_splitter_positions(number[0],paths,path+'0')
        get_splitter_positions(number[1],paths,path+'1')

def split(number,path):
    curr = number
    for p in to_digits(path[:-1]):
        curr = curr[p]
    l = floor(curr[int(path[-1])]/2)
    r = ceil(curr[int(path[-1])]/2)
    curr[int(path[-1])] = [l,r]

def print2(list):
    root = Node(-1)
    treeify(list,root)
    print(root) 

print(rows[0])
check = True
current = rows[0]
for i in range(len(rows)-1):
    current = [current, rows[i+1]]
    exploded, splitted = True, True
    while exploded or splitted:
        exploded = False
        splitted = False

        digits = []
        get_digit_positions(current, digits, '')

        exploders = []
        get_exploder_positions(current,exploders,'')
        
        for exploder in exploders:
            e1, e2 = get_numbers_from_exploder(current,exploder)
            remove_exploder(current,exploder)
            digits = []
            get_digit_positions(current,digits,'')
            s = list(map(lambda x: int(str(x).ljust(8).replace(' ','0'),2) < int(str(exploder).ljust(8).replace(' ','0'),2), digits))
            l = sum(s)-1
            try:
                if l < 0:
                    raise
                left_digit = digits[l]
                add_to_digit(current,left_digit,e1)
            except:
                pass
            try:
                right_digit = digits[l+2]
                add_to_digit(current,right_digit,e2)
            except:
                pass
            exploded = True
        splitters = []
        get_splitter_positions(current,splitters,'')
        for splitter in splitters:
            split(current,splitter)
            splitted = True
            break
print(current)

def sum2(num):
    s = 0
    if isinstance(num[0],list):
        s += 3*sum2(num[0])
    else:
        s += 3*num[0]
    
    if isinstance(num[1],list):
        s += 2*sum2(num[1])
    else:
        s += 2*num[1]

    return s

print(sum2(current))
max_mag = 0
for i in range(len(rows)):
    for j in range(len(rows)):
        rows = [eval(row) for row in data.split('\n')]
        ny_i = eval(str(rows[i]))
        ny_j = eval(str(rows[j]))
        current = [ny_i, ny_j]
        a = 0
        exploded, splitted = True, True
        while exploded or splitted:
            a+= 1
            exploded = False
            splitted = False

            digits = []
            get_digit_positions(current, digits, '')

            exploders = []
            get_exploder_positions(current,exploders,'')
            
            for exploder in exploders:
                e1, e2 = get_numbers_from_exploder(current,exploder)
                remove_exploder(current,exploder)
                digits = []
                get_digit_positions(current,digits,'')
                s = list(map(lambda x: int(str(x).ljust(8).replace(' ','0'),2) < int(str(exploder).ljust(8).replace(' ','0'),2), digits))
                l = sum(s)-1
                try:
                    if l < 0:
                        raise
                    left_digit = digits[l]
                    add_to_digit(current,left_digit,e1)
                except:
                    pass
                try:
                    right_digit = digits[l+2]
                    add_to_digit(current,right_digit,e2)
                except:
                    pass
                exploded = True
            splitters = []
            get_splitter_positions(current,splitters,'')
            for splitter in splitters:
                split(current,splitter)
                splitted = True
                break
            
        mag = sum2(current)
        if mag > max_mag:
            max_mag = mag

print(max_mag)