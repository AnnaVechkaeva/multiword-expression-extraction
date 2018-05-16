import re

de_file = open('corpus.MWE', encoding = 'utf-8')
en_file = open('corpus.src', encoding = 'utf-8')

de = []
en = []


for i in de_file:
    de.append(i)
    
for i in en_file:
    en.append(i)
    
for i in range(len(en)):
    if en[i] == '\n':
        compel = re.search('(Herr|Frau|Sehr geehrte|Werte|).*!', de[i])
        init_coma = re.search('^,', de[i])
        if compel is not None:
            de[i+1] = de[i][:-1] + ' ' + de[i+1]
            de[i] = 'EMPTY LINE'
            en[i] = 'EMPTY LINE'
        elif de[i] == '.\n' or de[i] == ').\n':
            de[i] = 'EMPTY LINE'
            en[i] = 'EMPTY LINE'
        elif init_coma is not None:
            de[i] = 'EMPTY LINE'
            en[i] = 'EMPTY LINE'
        else:
            de[i] = 'EMPTY LINE'
            de[i-1] = 'EMPTY LINE'
            de[i+1] = 'EMPTY LINE'
            en[i] = 'EMPTY LINE'
            en[i-1] = 'EMPTY LINE'
            en[i+1] = 'EMPTY LINE'

for i in range(len(de)):
    if de[i] == '\n':
        if en[i] == '.\n' or en[i] == ').\n':
            de[i] = 'EMPTY LINE'
            en[i] = 'EMPTY LINE'
        else:
            de[i] = 'EMPTY LINE'
            de[i-1] = 'EMPTY LINE'
            de[i+1] = 'EMPTY LINE'
            en[i] = 'EMPTY LINE'
            en[i-1] = 'EMPTY LINE'
            en[i+1] = 'EMPTY LINE'

de = list(filter(lambda x: x!= 'EMPTY LINE', de))
en = list(filter(lambda x: x!= 'EMPTY LINE', en))

de_clean = open('de', 'w', encoding = 'utf-8')
en_clean = open('en', 'w', encoding = 'utf-8')

for i in de:
    de_clean.write(i)
for i in en:
    en_clean.write(i)

de_clean.close()
en_clean.close()
print('Готово!')
