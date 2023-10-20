with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')
inputs = list(map(lambda x: (x[0].split(),x[1].split()),[row.split(' | ') for row in rows]))

def inv(letters):
    res = 'abcdefg'
    for letter in letters:
        res = res.replace(letter,'')
    return res

def remove_letters(letters, remove):
    for c in remove:
        letters = letters.replace(c,'')
    return letters

def intersect_letters(current,new):
    res = ''
    for c1 in current:
        for c2 in new:
            if c1 == c2:
                res += c1
    return res

numbers = {1: 'cf',
           2: 'acdeg',
           3: 'acdfg',
           4: 'bcdf',
           5: 'abdfg',
           6: 'abdefg',
           7: 'acf',
           8: 'abcdefg',
           9: 'abcdfg'}

def any_letter_in(s1, s2):
    for c1 in s1:
        for c2 in s2:
            if c1 == c2:
                return True
    return False

def all_letters_in(s1, s2):
    sum = 0
    for c1 in s1:
        for c2 in s2:
            if c1 == c2:
                sum += 1
    return len(s2) == sum

decoded = []
for input in inputs:
    possible = {'a': 'abcdefg',
                'b': 'abcdefg',
                'c': 'abcdefg',
                'd': 'abcdefg',
                'e': 'abcdefg',
                'f': 'abcdefg',
                'g': 'abcdefg'}

    def mark_known(number,digit):
        for letter in numbers[number]:
            possible[letter] = intersect_letters(possible[letter],digit)
        for letter in inv(numbers[number]):
            possible[letter] = remove_letters(possible[letter],digit)

    done = False
    while not done:
        len6_digits = []
        len5_digits = []
        for digit in input[0]:
            if len(digit) == 2:
                mark_known(1,digit)
            elif len(digit) == 3:
                mark_known(7,digit)
            elif len(digit) == 4:
                mark_known(4,digit)
            elif len(digit) == 5:
                len5_digits.append(digit)
            elif len(digit) == 6:
                len6_digits.append(digit)
                
        for digit in len5_digits:
            if all_letters_in(digit, possible['c']) and all_letters_in(digit, possible['f']):
                mark_known(3,digit)
            elif (len(possible['b']) == 1) and any_letter_in(digit,possible['b']):
                mark_known(5,digit)

        done = True        
        for key, item in possible.items():
            if len(item) > 1:
                done = False

    for digit in input[1]:
        if len(digit) == 2:
            d = 1
        elif len(digit) == 3:
            d = 7
        elif len(digit) == 4:
            d = 4
        elif len(digit) == 5:
            if possible['b'] in digit:
                d = 5
            elif possible['f'] in digit:
                d = 3
            elif possible['c'] in digit:
                d = 2
        elif len(digit) == 6:
            if not possible['d'] in digit:
                d = 0
            elif not possible['c'] in digit:
                d = 6
            elif not possible['e'] in digit:
                d = 9
        elif len(digit) == 7:
            d = 8
        decoded.append(d)
sum = 0
for i, n in enumerate(reversed(decoded)):
    sum += n*(10**(i%4))
print(sum)