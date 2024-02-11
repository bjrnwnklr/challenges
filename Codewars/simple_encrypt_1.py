def decrypt(text, n):
    if text and n > 0:
        for _ in range(n):
            mid = len(text) // 2
            e = text[-1] if len(text) % 2 != 0 else ''
            text = ''.join([text[i+mid] + text[i] for i in range(0, mid)]) + e
    return text


def encrypt(text, n):
    if text and n > 0:
        for _ in range(n):
            text = ''.join([text[i] for i in range(1, len(text), 2)]) + ''.join([text[i] for i in range(0, len(text), 2)])
    return text


