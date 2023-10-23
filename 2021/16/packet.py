with open("input.txt",'r') as f:
    data = f.read()
data = ''.join([bin(int(value,16))[2:].rjust(4).replace(' ','0') for value in data])
# data = '110100101111111000101000'
#         VVVTTTAAAAABBBBBCCCCC
# data = '11101110000000001101010000001100100000100011000001100000'
#         VVVTTTILLLLLLLLLLLVVVTTTAAAAAVVVTTTAAAAAVVVTTTAAAAA
# data = '00111000000000000110111101000101001010010001001000000000'
#         VVVTTTILLLLLLLLLLLLLLLVVVTTTAAAAAVVVTTTAAAAABBBBB


# 0101001000100100
# BBBBBBBBBBBBBBBB
# VVVTTTAAAAABBBBB
def to_str(list):
    return [str(v) for v in list]

operator = dict()
operator[0] = lambda x: eval('+'.join(to_str(x)))
operator[1] = lambda x: eval('*'.join(to_str(x)))
operator[2] = lambda x: min(x)
operator[3] = lambda x: max(x)
operator[5] = lambda x: 1 if x[0] >  x[1] else 0
operator[6] = lambda x: 1 if x[0] <  x[1] else 0
operator[7] = lambda x: 1 if x[0] == x[1] else 0

def evaluate(packet, index):
    if index+11 > len(packet):
        return 0, 0
    v = int(packet[index:index+3],2)
    t = int(packet[index+3:index+6],2)
    index += 6
    res = 0
    if t == 4:
        while True:
            res *= 16
            res += int(packet[index+1:index+5],2)
            index += 5
            if packet[index-5] == '0':
                break
    else:
        sub = []
        if packet[index] == '1':
            packets = int(packet[index+1:index+12],2)
            print('packets:',packets)
            i = 0
            index+=12
            while i < packets: 
                tmp_res, tmp_index = evaluate(packet,index)
                sub.append(tmp_res)
                index = tmp_index
                i += 1
        else:
            size = int(packet[index+1:index+16],2)
            print('size:',size)
            i = 0
            index+=16
            while i < size:
                tmp_index = index
                tmp_res, index = evaluate(packet,index)
                sub.append(tmp_res)
                i += index - tmp_index
        res = operator[t](sub)
    return res, index

print(evaluate(data,0))