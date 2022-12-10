with open("input.txt",'r') as f:
    data = f.read()

def find_signal_start(size):
    i, counter = 0, 0
    while i < len(data) - size - 1 and counter < size:
        if data[i] not in data[i+1:i+size-counter]:
            counter += 1
        else:
            counter = 0
        i += 1
    return i

print(find_signal_start(4))
print(find_signal_start(14))