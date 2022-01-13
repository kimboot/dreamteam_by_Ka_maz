# License dream team by ka maz
# project by xepaerZ & kulinarrr

from string import *

def main(FileName):
    FileREF = open(FileName)
    CheckWord = ''
    Censor = False
    Result = ''
    for line in FileREF:
        for c in line:
            if Censor == True:
                CheckWord = CheckWord + c
                if len(CheckWord) == 3:
                    if not CheckWord.rfind('go') == -1:
                        Result = Result + CheckWord.replace('go', '')
                        CheckWord = ''
                    else:
                        Censor = False
                        Result = Result + '***' + CheckWord
                        CheckWord = ''
            else:
                CheckWord = CheckWord + c
                if len(CheckWord) == 4:
                    if not CheckWord.rfind('ogo') == -1:
                        Censor = True
                        Result = Result + CheckWord.replace('ogo', '')
                        CheckWord = ''
                    else:
                        Result = Result + CheckWord
                        CheckWord = ''

    
    with open ('new_test.txt', 'w') as file:
        file.write(Result)

if __name__ == "__main__":
    main('test.txt')
