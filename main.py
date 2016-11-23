import wfa

f = open('遇蛇Chapter1c.txt', 'r')
fsentence = str(f.read())
wfa.WFA(fsentence, 10)

sentence = '水中映著彩霞，水面游著花鴨。霞是五彩霞，鴨是麻花鴨。麻花鴨游進五彩霞，五彩霞網住麻花鴨。樂壞了鴨，拍碎了霞，分不清是鴨還是霞。'
wfa.WFA(sentence)

fe = open('sonnets.txt', 'r')
fesentence = str(fe.read())
wfa.WFAE(fesentence, 6)