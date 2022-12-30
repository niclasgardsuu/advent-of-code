with open('test.txt') as f:
    data = f.read()
decimal, snafu = data.split('\n\n')
decimal = decimal.split('\n')
decimal = list(map(int,decimal))
snafu = snafu.split('\n')

print(decimal, snafu)

def arr_to_str(arr):
    if arr[0] == 0: # it could possibly still include the initial placeholder 0
        arr = arr[1:]
    s = ''
    for e in arr:
        s += str(e)
    
    return s

def snafu_to_decimal(snafu):
    decimal = 0
    for i in range(len(snafu)):
        n = 0
        if snafu[i] == '=':
            n = -2
        elif snafu[i] == '-':
            n = -1
        elif snafu[i] == '0':
            n = 0
        elif snafu[i] == '1':
            n = 1
        elif snafu[i] == '2':
            n = 2
        decimal += (5**(len(snafu)-1-i))*n
    return decimal

def decimal_to_snafu(decimal):
    # first convert to base 5
    length = 0
    for n in range(0,1000):
        if decimal < (5**n):
            length = n
            break

    # assign base 5 symbols
    snafu = [0] # 0 is placeholder for when converting to snafu
    for n in range(length):
        symbol = decimal // 5**(length-n-1)
        snafu.append(symbol)
        decimal -=  symbol * (5**(length-n-1))
    
    # convert to snafu
    for n in reversed(range(1, length+1)):
        # first add any overflow to next symbol
        snafu[n-1] += snafu[n] // 5
        snafu[n] = snafu[n] % 5

        # convert to snafu values [-2, -1, 0, 1, 2]
        if snafu[n] >= 3:
            snafu[n-1] += 1
            snafu[n] = snafu[n] - 5
        
    # snafu representation
    for i in range(length+1):
        if snafu[i] == -1:
            snafu[i] = '-'
        elif snafu[i] == -2:
            snafu[i] = '='
    snafu = arr_to_str(snafu)

    return snafu
    
print("SNAFU TO DECIMAL:")
for s, d in zip(snafu,decimal):
    decimalized = snafu_to_decimal(s)
    print(s,'==',d)
    try:
        assert(decimalized == d)
    except:
        print(decimalized, "does not equal", d)
        exit(1)

print("\nDECIMAL TO SNAFU:")
for s, d in zip(snafu,decimal):
    snafulized = decimal_to_snafu(d)
    print(d,'==',s)
    try:
        assert(s == snafulized)
    except:
        print(snafulized, "does not equal", s)
        exit(1)

## Now I know my functions work lol

with open('input.txt') as f:
    data = f.read()
snafus = data.split('\n')
print("\nTESTS DONE\n")

sum = sum(map(snafu_to_decimal,snafus)) 
print(sum)
print(decimal_to_snafu(sum))