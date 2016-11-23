from operator import itemgetter
import re

def list2freqdict(mylist):
    mydict = dict()
    for ch in mylist:
        mydict[ch]=mydict.get(ch,0)+1
    return mydict

def list2bigram(mylist):
    return [mylist[i:i+2] for i in range(0, len(mylist)-1)]

def list2trigram(mylist):
    return [mylist[i:i+3] for i in range(0, len(mylist)-2)]

def bigram2freqdict(mybigram):
    mydict = dict()
    for (ch1, ch2) in mybigram:
        mydict[(ch1, ch2)] = mydict.get((ch1,ch2),0)+1
    return mydict

def trigram2freqdict(mytrigram):
    mydict=dict()
    for (ch1, ch2, ch3) in mytrigram:
        mydict[(ch1, ch2, ch3)] = mydict.get((ch1, ch2, ch3), 0)+1
    return mydict

def freq2report(freqlist):
    chs = str()
    print('Char(s)\tCount')
    print('=============')
    for (token, num) in freqlist:
        for ch in token:
            chs = chs+ch
        print(chs, '\t', num)
        chs = ''
    return

def WFAE(sentence, ResultNum = 5):
    chlist = sentence.split()
    chfreqdict = list2freqdict(chlist)
    chfreqsorted = sorted(chfreqdict.items(), key=itemgetter(1), reverse=True)
    chbigram = list2bigram(chlist)
    chtrigram = list2trigram(chlist)

    bigramfreqdict=bigram2freqdict(chbigram)
    trigramfreqdict=trigram2freqdict(chtrigram)

    bigramfreqsorted=sorted(bigramfreqdict.items(), key=itemgetter(1), reverse=True)
    trigramfreqsorted=sorted(trigramfreqdict.items(), key=itemgetter(1), reverse=True)

    freq2report(chfreqsorted[:ResultNum])
    freq2report(bigramfreqsorted[:ResultNum])
    freq2report(trigramfreqsorted[:ResultNum])

def WFA(sentence, ResultNum = 5):
    chlist = [ch for ch in sentence]
    chfreqdict = list2freqdict(chlist)
    chfreqsorted = sorted(chfreqdict.items(), key=itemgetter(1), reverse=True)  # 把結果排序

    '''
    Frequency Distribution of Bigrams and Trigrams
    N-gram是自然語言處理常用到的方法，一般是用來計算共現(collocation)。
    在英文中可以用來計算word與word之間的共現關係，中文則比較常用來計算字與字之見的共現關係，
    對於斷詞(segmentation)或是計算詞彙的孳生性(productivity)來說非常重要。
    chbigram 與 chtrigram 就是在處理這個問題
    '''

    chbigram = list2bigram(chlist)
    chtrigram = list2trigram(chlist)

    #  計算collocation頻率
    bigramfreqdict=bigram2freqdict(chbigram)
    trigramfreqdict=trigram2freqdict(chtrigram)

    #  排序
    bigramfreqsorted=sorted(bigramfreqdict.items(), key=itemgetter(1), reverse=True)
    trigramfreqsorted=sorted(trigramfreqdict.items(), key=itemgetter(1), reverse=True)
    #print(bigramfreqsorted[:5])
    #print(trigramfreqsorted[:5])

    #  整理列印
    freq2report(chfreqsorted[:ResultNum])
    freq2report(bigramfreqsorted[:ResultNum])
    freq2report(trigramfreqsorted[:ResultNum])

