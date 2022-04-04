import nltk
import pymorphy2
import numpy as np

def TextProcessing(TextFile):
    morph = pymorphy2.MorphAnalyzer()
    
    File = open(TextFile, "r", encoding="utf-8")
    Text = File.read()

    TextTokens = nltk.word_tokenize(Text) # Токенизация текста

    Result = ''

    for word in TextTokens:
        p = morph.parse(word)[0]
        Result = Result + "\n" + word + " " + str(p.tag)

    with open("Result.txt", "a", encoding="utf-8") as file:
        file.write(Result)     

def Statistics():
    nouns = 0.0
    verbs = 0.0
    global adj
    adj = 0.0
    global prcl
    prcl = 0.0
    global npro
    npro = 0.0
    global total_lines
    total_lines = 0.0 
    sent_length_count = 0.0
    global verb_noun 
    verb_noun = 0.0
    noun_noun = 0.0
    global noun_noun_gen
    noun_noun_gen = 0.0 
    global dyn_stat 
    dyn_stat = 0.0
    verb_adv = 0.0
    grnd_noun = 0.0
    grnd_adv = 0.0
    adj_noun = 0.0

    global sent
    sent = []
    words = []

    File = open("Result.txt", "r", encoding="utf-8")
    lines = File.readlines()

    for index, item in enumerate(lines):
        next_index = index + 1

        if item.find("NOUN") != -1:
            nouns += 1
        elif ((item.find('VERB') != -1) or (item.find('INFN') != -1) or (item.find('GRND') != -1)):
            verbs += 1
        elif item.find ('ADJF') != -1:
            adj += 1
        elif item.find ('PRCL') != -1:
            prcl += 1
        elif item.find ('NPRO') != -1:
            npro += 1
        if next_index < len(lines):
            next_item = lines[index+1]
            if ((item.find ('NOUN') != -1) and (next_item.find('NOUN') != -1)) == True:
                noun_noun += 1
                if (next_item.find('gent') != -1):
                    noun_noun_gen += 1
            if (((item.find ('NOUN') != -1) and (next_item.find('VERB') != -1)) or ((item.find ('VERB') != -1) and (next_item.find('NOUN') != -1))) == True:
                verb_noun += 1
            if (((item.find ('ADVB') != -1) and (next_item.find('VERB') != -1)) or ((item.find ('VERB') != -1) and (next_item.find('ADVB') != -1))) == True:
                verb_adv += 1
            if ((item.find ('GRND') != -1) and (next_item.find('NOUN') != -1)) == True:
                grnd_noun += 1
            if (((item.find ('GRND') != -1) and (next_item.find('ADVB') != -1)) or ((item.find ('ADVB') != -1) and (next_item.find('GRND') != -1))) == True:
                grnd_adv += 1
            if ((item.find ('ADJF') != -1) and (next_item.find('NOUN') != -1)) == True:
                adj_noun += 1
        if ((item.find ('sent') == -1) and (item.find('PNCT') == -1)) :
            total_lines += 1
            sent_length_count += 1
            if ((item.find('LATN') == -1) and (item.find('NUMB') == -1) and (item.find('ROMN') == -1)) :
                pass
                #word_stub = item[(item.index('\t') + 1):]
                #word = word_stub[:word_stub.index('\t')]
                #words.append(float(len(word)))
            elif (item.find ('sent') != -1):
                if sent_length_count != 0.0:
                    sent.append(sent_length_count)
                sent_length_count = 0.0

    dyn_stat = ((verb_noun + verb_adv + grnd_noun + grnd_adv)/(noun_noun + adj_noun))

def style():
    if (((np.asarray(sent).sum()/float(len(sent))) >= 18) and (dyn_stat <= 0.1)):
        print (u'Скорее всего, это деловой текст')
    elif (((npro/total_lines) >= 0.03) and ((prcl/total_lines) >= 0.02)):
        print (u'Скорее всего, это художественный текст')
    elif ((((adj/total_lines) >= 0.1) and ((adj/total_lines) <= 0.2)) and ((prcl/total_lines) <= 0.02) and ((dyn_stat) <= 0.32) and (((npro/total_lines) >= 0.0038) and ((npro/total_lines) <= 0.0231))):
        print (u'Скорее всего, это научный текст')
    else:
        print (u'Скорее всего, это публицистический текст')

def Genres(TextFile):
    TextProcessing(TextFile)
    Statistics()
    style()
    
if __name__ == "__main__":
    Genres('test.txt')
