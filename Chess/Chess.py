
a = 4 # вертикально
b = 5 # горизонтально
c = 3 # вертикально
d = 4 # горизонтально

if a == c or b == d:
    print("Ладья угрожает")

if a - c == b - d:
    print("Слон угрожает")

if abs(a - c) == 1 or abs(b - d) == 1:
    print("Король попадает на поле")

if (a - c) == (b - d) or a == b or c == d:
    print("Ферзь угрожает")

if (abs(abs(a - c) - 2) == 0) and (abs(abs(b - d) - 1) == 0) or (abs(abs(a - c) - 1) == 0) and (abs(abs(b - d) - 2) == 0):
    print("Конь угрожает")

if a - c == 1 or b - d == 1:
    print("Белая пешка попадает на поле")
if a - c == d - b:
    print("Белая пешка попадает на поле когда бъет противника")

if a - c == -1 or b - d == -1:
    print("Черная пешка попадает на поле")
if a - c == b - d:
    print("Черная пешка попадает на поле когда бъет противника")

