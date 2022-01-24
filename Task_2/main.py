# License dream team by ka maz
# project by xepaerZ & kulinarrr
#task 2



Number_TShirts = {'s':1,'m':0,'l':1,'xl':0,'xxl':0,'xxxl':1}
Number_Participants = 3
Getter_TShirts = ''
schetchik = 0
rashod = 0

while schetchik < Number_Participants:
    Getter_TShirts = input("Введите размер фуболки: s, m, l, xl, xxl, xxxl ")
    if Getter_TShirts == "s":
        if Number_TShirts.get(Getter_TShirts) > 0 :
            Number_TShirts[Getter_TShirts] = Number_TShirts.get(Getter_TShirts) - 1
            print("Выдана одна футболка размера :", Getter_TShirts)
            schetchik += 1
        else:
            print("Нет размера")
    elif Getter_TShirts == "m":
        if Number_TShirts.get(Getter_TShirts) > 0 :
            Number_TShirts[Getter_TShirts] = Number_TShirts.get(Getter_TShirts) - 1
            print("Выдана одна футболка размера :", Getter_TShirts)
            schetchik += 1
        else:
            print("Нет размера")
    elif Getter_TShirts == "l":
        if Number_TShirts.get(Getter_TShirts) > 0 :
            Number_TShirts[Getter_TShirts] = Number_TShirts.get(Getter_TShirts) - 1
            print("Выдана одна футболка размера :", Getter_TShirts)
            schetchik += 1
        else:
            print("Нет размера")

    elif Getter_TShirts == "xl":
        if Number_TShirts.get(Getter_TShirts) > 0 :
            Number_TShirts[Getter_TShirts] = Number_TShirts.get(Getter_TShirts) - 1
            print("Выдана одна футболка размера :", Getter_TShirts)
            schetchik += 1
        else:
            print("Нет размера")

    elif Getter_TShirts == "xxl":
        if Number_TShirts.get(Getter_TShirts) > 0 :
            Number_TShirts[Getter_TShirts] = Number_TShirts.get(Getter_TShirts) - 1
            print("Выдана одна футболка размера :", Getter_TShirts)
            schetchik += 1
        else:
            print("Нет размера")
    elif Getter_TShirts == "xxxl":
        if Number_TShirts.get(Getter_TShirts) > 0 :
            Number_TShirts[Getter_TShirts] = Number_TShirts.get(Getter_TShirts) - 1
            print("Выдана одна футболка размера :", Getter_TShirts)
            schetchik += 1
        else:
            print("Нет размера")
    else:
        print("Введите правильный аргумент")

