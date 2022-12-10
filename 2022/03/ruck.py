with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')

def char_to_value(char):
    order = ord(char)
    if order < 97:
        return order - 38 # ascii of A is 65, which should return 27
    else:
        return order - 96 # ascii of a is 97, which should return 1

def split(list):
    return [list[:int(len(list)/2)],list[int(len(list)/2):]]

def group(list, size):
    grouped_list = []
    for group in (list[i:i+size] for i in range(0,int(len(list)),size)):
        grouped_list.append(group)
    return grouped_list

sum = 0
for sack in rows:
    compartments = split(sack)
    for item in compartments[0]:
        if item in compartments[1]:
            sum += char_to_value(item)
            break

sum2 = 0
for sacks in group(rows,3):
    for item in sacks[0]:
        if item in sacks[1] and \
           item in sacks[2]:
            sum2 += char_to_value(item)
            break

print(sum)  
print(sum2)  