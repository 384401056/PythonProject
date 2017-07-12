class BitsMask(int):

    def AND(self,bm):
        return BitsMask(self & bm)

    def OR(self,bm):
        return BitsMask(self | bm)

    def NOT(self):
        return BitsMask(~self)


# b = BitsMask()
# print(b)
# print(bin(b.NOT() & 0xF))
# b2 = BitsMask(0b10101100)
# print(bin(b2))