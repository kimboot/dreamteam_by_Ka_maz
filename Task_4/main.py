# License dream team by ka maz
# project by xepaerZ & kulinarrr
#task_4

numbers = []

def check_number(number_1, number_2):
    if number_1 == number_2:
        print('YES')

    elif number_1 > number_2:
        print('NO')
    else:
        if number_2[len(number_2) - 1] == '1':
            numbers.append(number_2[:len(number_2) - 1])
            check_number(number_1, number_2[:len(number_2) - 1])
        elif int(number_2[len(number_2) - 1]) % 2 == 0:
            numbers.append(str(int(number_2) // 2))
            check_number(number_1, str(int(number_2) // 2))
        else:
            print('NO')

def main():
    number_1 = input()
    number_2 = input()
    check_number(number_1,number_2)
    print(number_1, numbers[::-1], number_2)

if __name__ == "__main__":
    main()