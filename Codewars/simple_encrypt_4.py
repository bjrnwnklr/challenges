'''
1. "qwertyuiop"
2. "asdfghjkl"
3. "zxcvbnm,."

'''
chars = ["qwertyuiop", "asdfghjkl", "zxcvbnm,.",
         "QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM<>"]
all_chars = set(''.join(chars))

def encrypt(text, encryptKey):
    offsets = [int(x) for x in '{:03d}'.format(encryptKey)]
    tmp_text = []
    for c in text:
        if c not in all_chars:
            tmp_text.append(c)
        else:
            for i, x in enumerate(chars):
                if c in x:
                    tmp_text.append(x[(x.index(c) + offsets[i % 3]) % len(x)])
                    break
    return ''.join(tmp_text)
    
def decrypt(text, encryptKey):
    offsets = [int(x) for x in '{:03d}'.format(encryptKey)]
    tmp_text = []
    for c in text:
        if c not in all_chars:
            tmp_text.append(c)
        else:
            for i, x in enumerate(chars):
                if c in x:
                    tmp_text.append(x[(x.index(c) - offsets[i % 3]) % len(x)])
                    break
    return ''.join(tmp_text)
    