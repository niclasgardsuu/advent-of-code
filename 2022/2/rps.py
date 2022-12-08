with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')

def char_to_rps_value(char):
    if char == 'A' or char == 'X':
        return 0
    elif char == 'B' or char == 'Y':
        return 1
    elif char == 'C' or char == 'Z':
        return 2

games = map(lambda x: (char_to_rps_value(x[0]),char_to_rps_value(x[2])), rows)

sum = 0
sum2 = 0
for game in games:
    if game[0] == (game[1] + 1) % 3:
        sum += 0
    elif (game[0] + 1) % 3 == game[1]:
        sum += 6
    else:
        sum += 3
    sum += game[1] + 1

    if game[1] == 0:
        sum2 += (game[0] - 1) % 3 + 1
    elif game[1] == 1:
        sum2 += game[0] + 3 + 1
    else:
        sum2 += (game[0] + 1) % 3 + 6 + 1

print(sum)
print(sum2)
