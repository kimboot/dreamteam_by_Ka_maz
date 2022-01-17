# License dream team by ka maz
# project by xepaerZ & kulinarrr
#task_3

def main(FileName):

    FileREF = open(FileName)
    Price = ''
    Price_int = 0
    Result = 0
    #Price_dec = int(Price - int(Price))[1:]
    count_num_dec = 0
    for line in FileREF:
        for c in line:
            if c == '.':
                Price = ''
            if c.isdigit() == True:
                Price = Price + c
                print(int(Price))








if __name__ == "__main__":
    main('test.txt')