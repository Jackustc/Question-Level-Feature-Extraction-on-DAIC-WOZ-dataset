# coding: utf-8
__author__ = 'Guohou Shan'
import csv
import sentimentcalculation
id = ['id']
label_binary = ['PHQ-8_binary']  # >10 is 1 or 0
label_continue = ['PHQ-8_score']
gender = ['Gender']
s_starttime = ['start_time']
s_endtime = ['s_endtime']
answer_time = ['answer_time']
sentence_num_answer= ['sentence_num_in_answer']
wordratio_sentence_answer = ['wordratio_sentence_answer']

sigh_ratio = ['sigh_ratio_sentence']
laugh_ratio = ['laugh_ratio_sentence']
sniffle_ratio = ['sinffle_ratio_sentence']
um_ratio = ['um_ratio_sentence']

neg_senti_ratio = ['neg_sentiment_ratio']
pos_senti_ratio = ['pos_sentiment_ratio']
sentiment = ['sentiment']
avg_adj_num = ['avg_adj_num']
avg_adv_num = ['avg_adv_num']
prp_ratio = ['personal pronoun ratio in sentence']

avg_pos_words = ['avg_pos_words']
avg_neg_words = ['avg_neg_words']
avg_dep_words = ['avg_dep_words']
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
    f_w = csv.reader(f)
    next(f_w)
    for row in f_w:
        #id.append(row[0])
        #label_binary.append(row[1])
        #label_continue.append(row[2])
        #gender.append(row[3])
        if int(row[0]) == 451 or int(row[0]) == 458 or int(row[0]) ==480: continue
        with open('Q&A/{}_Q&A.CSV'.format(row[0]),'r',encoding='utf-8') as f1:
            print(row[0])
            wordcount = 0
            len_time = 0
            sentence_num = 0
            pos_num = 0
            neg_num = 0
            pos_num1 = 0
            neg_num1 = 0
            dep_num = 0
            senti = 0
            adj_num = 0
            adv_num = 0
            prp = 0
            f_w1 = csv.reader(f1)
            next(f_w1)
            sigh_num = 0
            laugh_num = 0
            sniffle_num = 0
            um_num = 0
            for row1 in f_w1:
                #print(row1[4])
                #print(count)
                if row1[0] == '': continue
                id.append(row1[0])
                label_binary.append(row1[1])
                label_continue.append(row1[2])
                gender.append(row1[3])
                s_starttime.append(row1[4])
                s_endtime.append(row1[5])
                answer_time.append(float(row1[5]) - float(row1[4]))
                sentence_num = len(row1[7].split('. '))
                if sentence_num == 0: continue
                wordcount = len(row1[7].split())
                sentence_num_answer.append(sentence_num)
                wordratio_sentence_answer.append(wordcount/sentence_num)

                lst = sentimentcalculation.sentivalue(row1[7]) # sentiment value, adjnum, advnum, prpnum
                for word in row1[7].split():
                    #print(word)
                    if word.startswith('<laughter'): laugh_num = laugh_num + 1
                    elif word.startswith('<sigh') : sigh_num = sigh_num + 1
                    elif word.startswith('<sniffle'): sniffle_num = sniffle_num +1
                    elif word == 'um': um_num = um_num + 1
                    if word in dep_word_list: dep_num = dep_num + 1
                    elif word in pos_word_list: pos_num1 = pos_num1+1
                    elif word in neg_word_list: neg_num1 = neg_num1 +1
                if lst[0]> 0: pos_num = pos_num +1
                elif lst[0]<0: neg_num = neg_num +1
                adj_num = lst[1]
                adv_num = lst[2]
                senti = lst[0]
                prp = lst[3]
                neg_senti_ratio.append(neg_num/sentence_num)
                pos_senti_ratio.append(pos_num/sentence_num)
                sentiment.append(senti)
                avg_adj_num.append(adj_num/sentence_num)
                avg_adv_num.append(adv_num/sentence_num)
                prp_ratio.append(prp/sentence_num)
                sigh_ratio.append(sigh_num/sentence_num)
                laugh_ratio.append(laugh_num/sentence_num)
                sniffle_ratio.append(sniffle_num/sentence_num)
                um_ratio.append(um_num/sentence_num)
                avg_pos_words.append(pos_num1/sentence_num)
                avg_neg_words.append(neg_num1/sentence_num)
                avg_dep_words.append(dep_num/sentence_num)
print('wordratio_sentence_answer',len(wordratio_sentence_answer))
print('sentiment',len(sentiment))
print('avg_adj_num',len(avg_adj_num))
print('avg_adv_num',len(avg_adv_num))
print('pos_senti_ratio',len(pos_senti_ratio))
print('neg_senti_ratio',len(neg_senti_ratio))
print('prp_ratio',len(prp_ratio))

with open('prepared_dataset_questionlevel.csv','w',encoding='utf-8',newline='') as f:
    f_w = csv.writer(f)
    for i in range(len(id)):
        row = [id[i],label_binary[i],label_continue[i],gender[i],s_starttime[i],s_endtime[i],sentence_num_answer[i]
               , wordratio_sentence_answer[i],sentiment[i], avg_adj_num[i],avg_adv_num[i],pos_senti_ratio[i],neg_senti_ratio[i],prp_ratio[i],
               um_ratio[i],sniffle_ratio[i],laugh_ratio[i],sigh_ratio[i],avg_pos_words[i],avg_neg_words[i],avg_dep_words[i]]
        #print(row)
        f_w.writerow(row)
