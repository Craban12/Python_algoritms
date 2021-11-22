n1=5
n2=6

bit_or = n1 | n2
bit_and = n1 & n2
bit_xor = n1 ^ n2

bln1 = n1 << 2
brn1 = n1 >> 2

print("ИЛИ", bin(bit_or))
print("И", bin(bit_and))
print("ТОЛЬКО ИЛИ", bin(bit_xor))

print('ЛЕВО', bin(bln1))
print('ПРАВО', bin(brn1))
