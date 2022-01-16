# License dream team by ka maz
# project by xepaerZ & kulinarrr
#task_3

def main(FileName):

    FileREF = open(FileName)
    Price = 0
    for line in FileREF:
        for c in line:
            if c == "." and not Price == 0:

            if c.isdigit() == True:
                    Price = Price +


if __name__ == "__main__":
    main('test.txt')