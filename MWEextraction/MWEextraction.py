import re

giza = open('giza.VA3.final', encoding = 'utf-8').read()
giza_sents = giza.split('#')
giza_sents = giza_sents[1:]

en_sents = []
deen_a = []
en_txt = ''

for allign in giza_sents:
    allign = allign.split('\n')
    en = allign[1].split()
    allign[2] = re.sub('\(', '', allign[2])
    de = allign[2].split(')')
    de = de[:-1]
    for n in range(len(de)):
        de[n] = re.sub('^ ', '', de[n])
        de[n] = re.sub('{ ', '{', de[n])
        de[n] = re.sub(' }', '}', de[n])
        de[n] = re.sub(' {', '!{', de[n])
        de[n] = re.sub('({|})', '', de[n])
        de[n] = de[n].split('!')
        de[n][1] = de[n][1].split()
        for i in range(len(de[n][1])):
            de[n][1][i] = int(de[n][1][i])
    en_sents.append(en)
    deen_a.append(de)

for sent in en_sents:
    for word in sent:
        en_txt += word + ' '
    en_txt += '\n'

# Finding all MWE candidates
print('Finding all MWE candidates')
MWE_candidates = []
for allign in range(len(deen_a)):
    for al in range(len(deen_a[allign])):
        word = deen_a[allign][al][0]
        al = deen_a[allign][al][1]
        if len(al) > 1:
            prev_is_MWE = 0
            MWE_candidat_n = []
            for i in range(len(al)-1):
                en_w1_n = al[i]
                en_w2_n = al[i+1]
                dist = en_w2_n - en_w1_n
                if dist < 2:
                    if prev_is_MWE == 0:
                        prev_is_MWE = 1
                        MWE_candidat_n.append([en_sents[allign][en_w1_n-1], en_sents[allign][en_w2_n-1]])
                    else:
                        MWE_candidat_n[len(MWE_candidat_n)-1].append(en_sents[allign][en_w2_n-1])
                else:
                    prev_is_MWE = 0
            count = 0
            for i in MWE_candidat_n:
                MWE_candidates.append(i)

# Creating frequency dictionary
print('Creating frequency dictionary')
MWE_cand_freq = {}
for i in MWE_candidates:
    i = ' '.join(i)
    if i in MWE_cand_freq:
        MWE_cand_freq[i] += 1
    else:
        MWE_cand_freq[i] = 1


# Finding for every MWE candidate their total frequency in the corpus, creating dictionary
print('Finding for every MWE candidate their total frequency in the corpus, creating dictionary')
MWE_in_txt = {}
cou = len(MWE_cand_freq)
cou0 = 0
for MWE_c in MWE_cand_freq:
    cou0 += 1 
    print(str(round(cou0/cou*100, 2))+'% done\r')
    for sent in en_sents:
        sent = ' '.join(sent)
        MWE_c_s = MWE_c.split()
        try:
            exps = re.findall(' ([a-z0-9]+ )?'.join(MWE_c_s), sent)
            if MWE_c in MWE_in_txt:
                MWE_in_txt[MWE_c] += len(exps)
            else:
                MWE_in_txt[MWE_c] = len(exps)
        except:
            pass

# Finding all the MWE candidates that ar alligned with one german word more often then with many words
print('Finding all the MWE candidates that ar alligned with one german word more often then with many words')
MWE_with_sw = []
for mwe in MWE_cand_freq:
    if mwe in MWE_in_txt:
        if MWE_in_txt[mwe] > 10:
            if MWE_cand_freq[mwe]/MWE_in_txt[mwe] > 0.5:
                MWE_with_sw.append(mwe)

# Dealing with Stop Words
print('Dealing with Stop Words')
sw = open('stop.wrd', encoding = 'utf-8').read().split()
MWE_final = []
for e in MWE_with_sw:
    des = 1
    expr = e.split()
    sw_count = 0
    for word in expr:
        if word in sw:
            sw_count += 1
    if len(expr) == 2 and sw_count > 0:
        des = 0
    elif sw_count/len(expr) >= 0.5:
        des = 0
    if des == 1:
        MWE_final.append(e)

print(len(MWE_final), 'MWE found')
out = open('MWElist.txt', 'w', encoding = 'utf-8')
for i in MWE_final:
    out.write(i+'\n')
out.close()
        


