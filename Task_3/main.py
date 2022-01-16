# License dream team by ka maz
# project by xepaerZ & kulinarrr
#task_3

def main(FileName):

    FileREF = open(FileName)
    Price = 0
    Price_dec = int(Price - int(Price))[1:]
    count_num_dec = 0
    for line in FileREF:
        for c in line:
            if c == "." and not Price == 0:

            if c.isdigit() == True:




if __name__ == "__main__":
    main('test.txt')