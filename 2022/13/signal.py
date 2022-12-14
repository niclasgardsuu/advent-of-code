with open("input.txt",'r') as f:
    data = f.read()
pairs = data.split('\n\n')
for i, pair in enumerate(pairs):
    p = pair.split('\n')
    p1 = eval(p[0])
    p2 = eval(p[1])
    pairs[i] = [p1, p2]

signals = data.replace('\n\n','\n').split('\n')
for i, signal in enumerate(signals):
    signals[i] = eval(signal)

def cut(l,r):
    length = min(len(l), len(r))
    return l[:length], r[:length]

def is_list(l):
    try:
        len(l)
    except:
        return False 
    return True

def is_right(left, right):
    if is_list(left) and is_list(right):
        left2, right2 = cut(left, right)
        broke = False
        for l,r in zip(left2,right2):
            check = is_right(l,r)
            if check == False:
                return False
            if check == True:
                broke = True
                break
        if broke:
            return True
        if len(left) < len(right):
            return True # den här raden gjorde mig galen för hitta inte de i instruktionerna förrän 10h senare >:(
        elif len(left) == len(right):
            return "Almost True :)"
        else:
            return False 
    elif is_list(left):
        return is_right(left, [right])
    elif is_list(right):
        return is_right([left],right)
    else:
        if left < right:
            return True
        elif left > right:
            return False
        else:
            return "Almost True :)"

sum = 0
for i, pair in enumerate(pairs):
    if is_right(pair[0],pair[1]) != False:
        sum += i+1

decoders = [1,2]
for signal in signals:
    if is_right(signal,[[2]]):
        decoders[0] += 1
    if is_right(signal,[[6]]):
        decoders[1] += 1
        
print(sum)
print(decoders[0], "*", decoders[1], "=", decoders[0]*decoders[1])