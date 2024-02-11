'''
For encrypting strings this region of chars is given (in this order!):

all letters (ascending, first all UpperCase, then all LowerCase)
all digits (ascending)
the following chars: ".,:;-?! '()$%&" and the '"'-char
These are 77 chars! (This region is zero-based.)

Write two methods: 

def encrypt(text)
def decrypt(encrypted_text)
Prechecks:

If the input-string has chars, that are not in the region, throw an Exception(C#, Python) or Error(JavaScript).
If the input-string is null or empty return exactly this value!
For building the encrypted string:

For every second char do a switch of the case.
For every char take the index from the region. Take the difference from the region-index of the char before (from the input text! Not from the fresh encrypted char before!). (Char2 = Char1-Char2)
Replace the original char by the char of the difference-value from the region. In this step the first letter of the text is unchanged.
Replace the first char by the mirror in the given region. ('A' -> '"', 'B' -> '&', ...)

'''
import string
chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + '.,:;-?! \'()$%&"'

def decrypt(text):
    if text and len(text) > 0:
        for c in text:
            if c not in chars:
                raise ValueError('%s not in chars!' % c)
        # reverse step 3 - return first char back
        text = chars[-1 * (chars.index(text[0]) + 1)] + text[1:]
        # reverse step 2: encr = orig(-1) - orig; orig = orig(-1) - encr
        tmp_text = [text[0]]
        for i in range(1, len(text)):
            tmp_text.append(chars[(chars.index(tmp_text[i-1]) - chars.index(text[i])) % 77])
        text = ''.join(tmp_text)
        # reverse step 1: swap cases
        text = ''.join([text[i].swapcase() if i % 2 else text[i] for i in range(len(text))])
    return text

def encrypt(text):
    if text and len(text) > 0:
        for c in text:
            if c not in chars:
                raise ValueError('%s not in chars!' % c)
        # step 1 - swap case of every 2nd char
        text = ''.join([text[i].swapcase() if i % 2 else text[i] for i in range(len(text))])
        # step 2 - replace letters
        text = ''.join([text[0]] + [chars[(chars.index(text[i-1]) - chars.index(text[i])) % 77] for i in range(1, len(text))])
        # step 3 - replace first char
        text = chars[-1 * (chars.index(text[0]) + 1)] + text[1:]
    return text
 
