# License dream team by ka maz
# project by xepaerZ & kulinarrr
#task_6


def can(v, g):
    list.sort(g)
    if g[0] <= v:
        return v - g[0]
    else:
        return -1

def main():
    n = 3 # Кол-во машин в прокате
    k = 1 # Кол-во заправок на пути до кинотеатра
    s = 8 # Дорога до кинотеатра
    t = 10 # Время до начала сеанса
    c = [10, 5, 11] # Стоимость аренды каждой машины
    v = [8, 7, 9] # Объем бака каждой машины
    g = [3] # Позиции заправок

    i = 0
    for j in c:
        if can(v[i], g) >= v[i]:
            if j < car:
                car = j
        i += 1
    
    print(j)


if __name__ == "__main__":
    main()