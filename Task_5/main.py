# License dream team by ka maz
# project by xepaerZ & kulinarrr
# task_5
def check_up(x, y, scene):
    while y >= 0:
        if scene[y][x] == 1:
            return True
        else:
            y -= 1
    return False


def check_down(x, y, scene, sizeY_scene):
    while y < sizeY_scene:
        if scene[y][x] == 1:
            return True
        else:
            y += 1
    return False


def check_left(x, y, scene):
    while x >= 0:
        if scene[y][x] == 1:
            return True
        else:
            x -= 1
    return False


def check_right(x, y, scene, sizeX_scene):
    while x < sizeX_scene:
        if scene[y][x] == 1:
            return True
        else:
            x += 1
    return False


def main():
    sizeX_scene = 4
    sizeY_scene = 2
    scene = [[0, 1, 0, 0], [1, 0, 1, 0]]
    count = 0
    x = -1
    y = -1
    for i in scene:
        y += 1
        x = -1
        for j in i:
            x += 1
            if not scene[y][x] == 1:
                if check_up(x, y, scene):
                    print(x + 1, y + 1)
                    count += 1
                if check_down(x, y, scene, sizeY_scene):
                    print(x + 1, y + 1)
                    count += 1
                if check_left(x, y, scene):
                    print(x + 1, y + 1)
                    count += 1
                if check_right(x, y, scene, sizeX_scene):
                    print(x + 1, y + 1)
                    count += 1
    print(count)

if __name__ == "__main__":
    main()
