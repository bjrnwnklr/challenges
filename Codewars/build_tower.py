def tower_builder(n):
    width = 1 + 2 * (n-1)
    out = []
    for i in range(1, n+1):
        s = i * 2 - 1
        blanks = (width - s) // 2
        out.append(' ' * blanks + '*' * s + ' ' * blanks)
    return out