print("Введите первую фигуру(белая).")
piece1 = str(input())
print("Введите координаты первой(белой) фигуры (вертикаль, горизонталь)")
a = int(input()) - 1
b = int(input()) - 1
print("Введите координаты хода.")
e = int(input()) - 1
f = int(input()) - 1
print("Введите вторую фигуру.")
piece2 = str(input())
print("Введите координаты второй(черной) фигуры (вертикаль, горизонталь)")
c = int(input()) - 1
d = int(input()) - 1

def Chess2(piece1,a,b,e,f):
    if piece1 == "Ладья":
        if a == e or b == f:
            print("Да")
        else:
            print("Нет")

    elif piece1 == "Слон":
        if a - e == b - f:
            print("Да")
        else:
            print("Нет")
    elif piece1 == "Король":
        if abs(a - e) == 1 or abs(b - f) == 1:
            print("Да")
        else:
            print("Нет")
    elif piece1 == "Ферзь":
        if (a - e) == (b - f) or a == e or b == f:
            print("Да")
        else:
            print("Нет")
    elif piece1 == "Пешка белая":
        if a - e == 1 or b - f == 1:
            print("Да")
        else:
            print("нет")
    elif piece1 == "Пешка черная":
        if a - e == -1 or b - f == -1:
            print("Да")
        else:
            print("Нет")
    elif piece1 == "Конь":
        if ((abs(abs(a - e) - 2) == 0) and (abs(abs(b - f) - 1) == 0)
                or (abs(abs(a - e) - 1) == 0) and (abs(abs(b - f) - 2) == 0)):
            print("Да")
        else:
            print("Нет")

Chess2(piece1,a,b,e,f)

def ChessCh(piece2,c,d,e,f):
    if piece2 == "Ладья":
        if c == e or d == f:
            print(", будет угрожать")
        else:
            print("")

    elif piece2 == "Слон":
        if c - e == d - f:
            print(", будет угрожать")
        else:
            print("")
    elif piece2 == "Король":
        if abs(c - e) == 1 or abs(d - f) == 1:
            print(", будет угрожать")
        else:
            print("")
    elif piece2 == "Ферзь":
        if (c - e) == (d - f) or c == e or d == f:
            print(", будет угрожать")
        else:
            print("")
    elif piece2 == "Пешка белая":
        if c - e == 1 or d - f == 1:
            print(", будет угрожать")
        else:
            print("")
    elif piece2 == "Пешка черная":
        if c - e == -1 or d - f == -1:
            print(", будет угрожать")
        else:
            print("")
    elif piece2 == "Конь":
        if ((abs(abs(c - e) - 2) == 0) and (abs(abs(d - f) - 1) == 0)
                or (abs(abs(c - e) - 1) == 0) and (abs(abs(d - f) - 2) == 0)):
            print(", будет угрожать")
        else:
            print("")

ChessCh(piece2, c, d, e, f)
