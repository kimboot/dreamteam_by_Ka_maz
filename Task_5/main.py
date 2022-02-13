# License dream team by ka maz
# project by xepaerZ & kulinarrr
#task_5
def check_up(index, scene):
    pass

def check_down(index, scene):
    pass

def check_left(index, scene):
    i = index
    while i >= len(scene) - 1:
        if scene[i] == 1:
            return True
        else:
            i -= 1
    return False

def check_right(index, scene, x):
    i = index
    while i <= x - 1:
        if scene[i] == 1:
            return True
        else:
            i += 1
    return False

def main():
    sizeX_scene = 4
    sizeY_scene = 2
    scene = [0, 1, 0, 0, 1, 0, 1, 0]
    count = 0
    i = 0
    while i <= len(scene) - 1:
        if not scene[i] == 1:
            if check_up(i, scene):
                count += 1
            if check_down(i, scene):
                count += 1
            if check_left(i, scene):
                count += 1
            if check_right(i, scene, sizeX_scene):
                count += 1   
        i += 1
    print(count)
if __name__ == "__main__":
    main()