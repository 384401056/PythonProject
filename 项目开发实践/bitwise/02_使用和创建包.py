import bits

print(bits.NOT(0b0101))
print(bin(bits.NOT(0b0101)))
print(bin(bits.NOT(0b0101) & 0xF))
print(bin(bits.AND(0b0101, 0b0011) & 0xF))
