with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')

part1 = 0
part2 = 0
for row in rows:
    
    digits = ''
    digits2 = ''
    i=0
    while i < len(row):
        if row[i].isdigit():
            digits += row[i]
            digits2 += row[i]
            i+=1
        else:
            if row[i:i+3] == 'one':
                digits2 += '1'
            elif row[i:i+3] == 'two':
                digits2 += '2'
            elif row[i:i+5] == 'three':
                digits2 += '3'
            elif row[i:i+4] == 'four':
                digits2 += '4'
            elif row[i:i+4] == 'five':
                digits2 += '5'
            elif row[i:i+3] == 'six':
                digits2 += '6'
            elif row[i:i+5] == 'seven':
                digits2 += '7'
            elif row[i:i+5] == 'eight':
                digits2 += '8'
            elif row[i:i+4] == 'nine':
                digits2 += '9'
            elif row[i:i+4] == 'zero':
                digits2 += '0'
            i+=1 # choke trodde att man inte skulle räkna två mergeade nummer.

    part1 += int(digits[0])*10 + int(digits[-1])
    part2 += int(digits2[0])*10 + int(digits2[-1])

print(part1)
print(part2)