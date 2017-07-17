# 导入bitswise包
import bitswise.bits as bits
from bitswise import bitsmask

print(bits)
print(bitsmask)

print(bin(bits.AND(0b00001,0b11110)))
b = bitsmask.BitsMask(0b00001)
print(bin(b.AND(0b11110)))