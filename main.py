# License dream team by ka maz
# project by xepaerZ & kulinarrr

from string import *

def countsymbol(FileName):
    FileREF = open(FileName)
    countletter = len(FileREF.read())
    return countletter

def main(FileName):

    FileREF = open(FileName)
    countletter = countsymbol(FileName)
    CheckWord = ''
    Censor = False
    Result = ''
    indexletter = 0

    for line in FileREF:
        for c in line:
            if Censor == True:
                CheckWord = CheckWord + c
                if len(CheckWord) == 2:
                    if not CheckWord.rfind('go') == -1:
                        Result = Result + CheckWord.replace('go', '')
                        CheckWord = ''
                    else:
                        Censor = False
                        Result = Result + '***' + CheckWord
                        CheckWord = ''
                elif indexletter + 2 > countletter:
                    if not CheckWord.rfind('go') == -1:
                        Result = Result + CheckWord.replace('go', '')
                        CheckWord = ''
                    else:
                        Censor = False
                        Result = Result + '***' + CheckWord
                        CheckWord = ''
            else:
                if  c == 'o' or c == 'g':
                    CheckWord = CheckWord + c
                    if len(CheckWord) == 3:
                        if not CheckWord.rfind('ogo') == -1:
                            Censor = True
                            Result = Result + CheckWord.replace('ogo', '')
                            CheckWord = ''
                        else:
                            Result = Result + CheckWord
                            CheckWord = ''
                    elif indexletter + 3 > countletter:
                        if not CheckWord.rfind('ogo') == -1:
                            Censor = True
                            Result = Result + CheckWord.replace('ogo', '')
                            CheckWord = ''
                        else:
                            Result = Result + CheckWord
                            CheckWord = ''
                else:
                    if not CheckWord == '':
                        Result = Result + CheckWord
                        CheckWord = ''
                    Result = Result + c

            indexletter += 1
    
    if Censor == True:
        Result = Result + '***'

    with open ('new_test.txt', 'w') as file:
        file.write(Result)

if __name__ == "__main__":
    main('test.txt')
