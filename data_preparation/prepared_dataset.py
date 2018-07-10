# coding: utf-8
__author__ = 'Guohou Shan'
import csv
import sentimentcalculation
id = ['id']
label_binary = ['PHQ-8_binary']  # >10 is 1 or 0
label_continue = ['PHQ-8_score']
gender = ['Gender']
avg_word_sententce= ['avg_word_in_sentence']
avg_len_time = ['avg_len_time']
total_sentence = ['total_sentence']
neg_senti_ratio = ['neg_sentiment_ratio']
pos_senti_ratio = ['pos_sentiment_ratio']
sentiment = ['sentiment']
avg_adj_num = ['avg_adj_num']
avg_adv_num = ['avg_adv_num']
prp_ratio = ['personal pronoun ratio in sentence']
sigh_ratio = ['sigh_ratio_sentence']
laugh_ratio = ['laugh_ratio_sentence']
sniffle_ratio = ['sinffle_ratio_sentence']
um_ratio = ['um_ratio_sentence']
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
        id.append(row[0])
        label_binary.append(row[1])
        label_continue.append(row[2])
        gender.append(row[3])
        with open('transcript data clean/{}_participant.CSV'.format(row[0]),'r',encoding='utf-8') as f1:
            count = 0
            len_sentence = 0
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
                #print(count)
                count = count+1
                len_sentence = len_sentence +len(row1[4].split())
                len_time = len_time + float(row1[2])
                sentence_num = sentence_num + len(row1[4].split('. '))
                lst = sentimentcalculation.sentivalue(row1[4]) # sentiment value, adjnum, advnum, prpnum
                for word in row1[4].split():
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
                adj_num = adj_num + lst[1]
                adv_num = adv_num + lst[2]
                senti = senti + lst[0]
                prp = prp + lst[3]
            avg_word_sententce .append(len_sentence/sentence_num)
            avg_len_time.append(len_time/count)
            total_sentence.append(sentence_num)
            neg_senti_ratio.append(neg_num/count)
            pos_senti_ratio.append(pos_num/count)
            sentiment.append(senti)
            avg_adj_num.append(adj_num/count)
            avg_adv_num.append(adv_num/count)
            prp_ratio.append(prp/sentence_num)
            sigh_ratio.append(sigh_num/sentence_num)
            laugh_ratio.append(laugh_num/sentence_num)
            sniffle_ratio.append(sniffle_num/sentence_num)
            um_ratio.append(um_num/sentence_num)
            avg_pos_words.append(pos_num1/count)
            avg_neg_words.append(neg_num1/count)
            avg_dep_words.append(dep_num/count)
with open('prepared_dataset.csv','w',encoding='utf-8',newline='') as f:
    f_w = csv.writer(f)
    for i in range(len(id)):
        row = [id[i],label_binary[i],label_continue[i],gender[i],avg_len_time[i],avg_word_sententce[i],total_sentence[i]
               , sentiment[i], avg_adj_num[i],avg_adv_num[i],pos_senti_ratio[i],neg_senti_ratio[i],prp_ratio[i],
               um_ratio[i],sniffle_ratio[i],laugh_ratio[i],sigh_ratio[i],avg_pos_words[i],avg_neg_words[i],avg_dep_words[i]]
        #print(row)
        f_w.writerow(row)
