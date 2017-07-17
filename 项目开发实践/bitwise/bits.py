def NOT(value):
    return ~value

def AND(value1,value2):
    return value1 & value2

def OR(value1,value2):
    return value1 | value2

def XOR(value1,value2):
    return value1^value2

def shiftLeft(value,num):
    return value << num

def shiftRight(value,num):
    return value >> num

def bit(value,idx):
    mask = 1 << idx # all 0 except idx
    return bool(value&1)

def setBit(value,idx):
    mask = 1 << idx # all 0 excpte idx
    return value | mask

def zeroBit(value,idx):
    mask = ~(1 << idx) # all 1 excpte idx
    return value & mask

def listBits(value):
    num = len(bin(value)) - 2
    result = []
    for n in range(num):
        result.append( 1 if bit(value,n) else 0)
    return list(reversed((result)))
