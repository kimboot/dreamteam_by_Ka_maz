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
                        Prices.append(Price)
                        Price = ''
                        AddPrice = False
                else:
                    Prices.append(Price)
                    Price = ''
                    AddPrice = False
    print(Prices)
    print(Pennies)
    return Prices, Pennies

def summ_price(Prices, Pennies):
    Summ = 0.0
    for c in Prices:
        Summ = Summ + float(c.replace('.', ''))
    for c in Pennies:
        if 10 <= float(c) <= 99:
            Summ = Summ + (float(c) / 100)

    print("Общая сумма чека: " + f"{Summ:,}")

def main(FileName):
    Prices, Pennies = scan_price(FileName)
    summ_price(Prices, Pennies)

if __name__ == "__main__":
    main('test.txt')