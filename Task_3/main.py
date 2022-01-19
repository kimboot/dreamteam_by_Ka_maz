# License dream team by ka maz
# project by xepaerZ & kulinarrr
#task_3

def scan_price(FileName):
    
    FileREF = open(FileName)
    Prices = []
    Pennies = []
    Price = ''
    AddPrice = False

    for line in FileREF:
        for c in line:
            if c.isdigit() == True or c == '.':
                AddPrice = True
                Price = Price + c
            elif AddPrice == True:
                if len(Price[Price.find('.')::-1]) == 3:
                    print(len(Price[Price.find('.')::-1]))
                    print(Price[Price.find('.')::1])
                    Pennies.append(Price[Price.find('.') + 1::1])
                    Prices.append(Price[0:Price.find('.')])
                    Price = ''
                    AddPrice = False
                else:
                    Prices.append(Price)
                    Price = ''
                    AddPrice = False
    print(Prices)
    return Prices

def summ_price(Prices):
    Summ = 0
    check_price = ''
    for c in Prices:
        pass


def main(FileName):
    summ_price(scan_price(FileName))

if __name__ == "__main__":
    main('test.txt')