#coding:utf-8
#instruction: this code is used for sentence level extraction
import csv
import sentimentcalculation
pos_word_list = []
neg_word_list = []
dep_word_list = []
with open('opinion-lexicon-English/positive-words.txt','r',encoding='utf-8') as f:
    for line in f.readlines():
        pos_word_list.append(str(line).strip())
    #print(pos_word_list)
with open('opinion-lexicon-English/negative-words.txt','r',encoding='utf-8') as f:
    for line in f.readlines():
        neg_word_list.append(str(line).strip())
with open('opinion-lexicon-English/depressedword.txt','r',encoding='utf-8') as f:
    for line in f.readlines():
        if len(line.split())==2:
            for ele in line.split()[1].split(','): dep_word_list.append(ele)
        else:dep_word_list.append(str(line).strip())

with open('transcript data clean/transcriptconent.csv','r',encoding='utf-8') as f:
    next(f)
    f_w = csv.reader(f)
    id = ['id']
    label_binary = ['PHQ-8_binary']  # >10 is 1 or 0
    label_continue = ['PHQ-8_score']
    gender = ['Gender']
    S_starttime = ['S_starttime']
    S_endtime = ['S_endtime']
    #Question = ['Question']
    #Sentence = ['Sentence']
    Sen_word_len = ['Sen_word_len']
    Sen_sentiment = ['Sen_sentiment']
    Sen_len_time = ['avg_len_time']
    Sen_sentiment = ['Sen_sentiment']
    Sen_adj_num = ['Sen_adj_num']
    Sen_adv_num = ['Sen_adv_num']
    Sen_prp_num = ['Sen_prp_num']
    Sen_sigh_num = ['Sen_sigh_num']
    Sen_laugh_num = ['Sen_laugh_num']
    Sen_sniffle_num = ['Sen_sniffle_num']
    Sen_um_num = ['Sen_um_num']
    Sen_pos_words = ['Sen_pos_words']
    Sen_neg_words = ['Sen_neg_words']
    Sen_dep_words = ['Sen_dep_words']
    for row in f_w:
        with open('transcript data clean/{}_TRANSCRIPT.csv'.format(row[0]),'r',encoding='utf-8') as f1:
            next(f1)
            f_w1 = csv.reader(f1)
            for row1 in f_w1:
                if len(row1)==0: continue
                line = row1[0].split('\t')
                if line[2]=='Participant':
                    id.append(row[0])
                    label_binary.append(row[1])
                    label_continue.append(row[2])
                    gender.append(row[3])
                    S_starttime.append(line[0])
                    S_endtime.append(line[1])
                    Sen_word_len.append(len(line[3].split()))
                    lst = sentimentcalculation.sentivalue(line[3])
                    Sen_sentiment.append(lst[0])
                    Sen_adj_num.append(lst[1])
                    Sen_adv_num.append(lst[2])
                    Sen_prp_num.append(lst[3])
                    for word in line[3].split():
                        laugh_num = 0
                        sigh_num = 0
                        sniffle_num=0
                        um_num=0
                        dep_num = 0
                        pos_num = 0
                        neg_num = 0
                        if word.startswith('<laughter'): laugh_num = laugh_num + 1
                        elif word.startswith('<sigh') : sigh_num = sigh_num + 1
                        elif word.startswith('<sniffle'): sniffle_num = sniffle_num +1
                        elif word == 'um': um_num = um_num + 1
                        if word in dep_word_list: dep_num = dep_num + 1
                        elif word in pos_word_list: pos_num = pos_num+1
                        elif word in neg_word_list: neg_num = neg_num +1
                    Sen_laugh_num.append(laugh_num)
                    Sen_sigh_num.append(sigh_num)
                    Sen_um_num.append(um_num)
                    Sen_sniffle_num.append(sniffle_num)
                    Sen_dep_words.append(dep_num)
                    Sen_pos_words.append(pos_num)
                    Sen_neg_words.append(neg_num)
        with open('combine/{}_textfeature.csv'.format(row[0]),'w',encoding='utf-8',newline='') as f2:
            f_w2 = csv.writer(f2)
            for i in range(len(id)):
                row2 = [id[i],label_binary[i],label_continue[i],gender[i],S_starttime[i],S_endtime[i],Sen_word_len[i],
                        Sen_sentiment[i],Sen_adj_num[i],Sen_adv_num[i],Sen_prp_num[i],Sen_laugh_num[i],
                        Sen_sigh_num[i],Sen_um_num[i],Sen_sniffle_num[i],Sen_dep_words[i],Sen_pos_words[i],
                        Sen_neg_words[i]]
                f_w2.writerow(row2)




