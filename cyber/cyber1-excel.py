u = ''.join([chr(x) for x in [101, 118, 105, 108, 45, 104, 97, 99, 107, 101, 114]])

u2 = ''.join([chr(x) for x in [46, 99, 104]])

            

sval = 0xf67 & 0x7CE

print(''.join([r'https://', u, str(sval), u2]))