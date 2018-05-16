import nltk, re

punctuation = ['!', ',', '.', ':', ';','(',')','[',']','?']

de_file = open('de', encoding = 'utf-8')
en_file = open('en', encoding = 'utf-8')

de_out = open('de.n', 'w', encoding = 'utf-8')
en_out = open('en.n', 'w', encoding = 'utf-8')

de = []
en = []
count = 0
print('Working on de')
for i in de_file:
    count += 1
    print('\r'+str(count))
    i = nltk.word_tokenize(i)
    for j in range(len(i)):
        i[j] = i[j].lower()
    for p in punctuation:
        if p in i:
            i = list(filter(lambda x: x!= p, i))
    i = ' '.join(i)
    de.append(i)

print('Working on en')
count = 0
for i in en_file:
    count += 1
    print('\r'+str(count))
    i = nltk.word_tokenize(i)
    for j in range(len(i)):
        i[j] = i[j].lower()
    for p in punctuation:
        if p in i:
            i = list(filter(lambda x: x!= p, i))
    i = ' '.join(i)
    en.append(i)
print('Writing!')
for i in range(len(de)):
    if de[i] != '' and en[i] != '':
        de_out.write(de[i]+'\n')
        en_out.write(en[i]+'\n')


de_out.close()
en_out.close()

print('Готово!')
