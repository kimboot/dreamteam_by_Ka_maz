import math

def zigzag_indexes(num_rows):
    yield (0, math.inf) #Вершины массива
    yield from zip(
        range(1, num_rows),# понижение
        range(2 * num_rows - 3, num_rows - 1, -1)# Повышение
    )
    yield (num_rows - 1, math.inf) # низ значений

def convert(s, num_rows):
    if num_rows == 1:
        return s
    zigzag_size = 2 * num_rows - 2
    return ''.join(
        (s[z+a] if z+a < len(s) else '') + (s[z+b] if z+b < len(s) else '')
        for a, b in zigzag_indexes(num_rows)
        for z in range(0, len(s), zigzag_size)
    )

print(convert('PAYPALISHIRING', 1))