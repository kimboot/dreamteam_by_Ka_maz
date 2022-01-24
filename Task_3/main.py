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
                if not Price.find('.') == -1:
                    if len(Price[Price.rfind('.'):len(Price) - 1]) == 2:
                        Pennies.append(Price[Price.rfind('.') + 1::1])
                        Prices.append(Price[0:Price.rfind('.')])
                        Price = ''
                        AddPrice = False
                    else:
                        Price = ''
                        AddPrice = False
                else:
                    Prices.append(Price)
                    Price = ''
                    AddPrice = False
    print(Prices)
    print(Pennies)
    return Prices

def summ_price(Prices):
    Summ = 0
    price = 0
    for c in Prices:
        for j in c:
            if j == '.':
                pass
    print(Summ)
def main(FileName):
    summ_price(scan_price(FileName))

if __name__ == "__main__":
    main('test.txt')