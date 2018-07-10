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

    for row in f_w:
        id = ['id']
        label_binary = ['PHQ-8_binary']  # >10 is 1 or 0
        label_continue = ['PHQ-8_score']
        gender = ['Gender']
        A_Sentence_num = ['A_Sentence_Num']
        A_word_num = ['A_word_num']
        A_sentiment= ['A_sentiment']
        A_neg_senti_ratio = ['A_neg_sentiment_ratio']
        A_pos_senti_ratio = ['A_pos_sentiment_ratio']
        A_avg_adj_num = ['A_avg_adj_num']
        A_avg_adv_num = ['A_avg_adv_num']
        A_prp_ratio = ['A_prp_ratio']
        A_sigh_ratio = ['A_sigh_ratio']
        A_laugh_ratio = ['A_laugh_ratio']
        A_sniffle_ratio = ['A_sinffle_ratio']
        A_um_ratio = ['A_um_ratio']
        A_avg_pos_words = ['A_avg_pos_words']
        A_avg_neg_words = ['A_avg_neg_words']
        A_avg_dep_words = ['A_avg_dep_words']

        bi = row[1]
        score=row[2]
        ans = ''
        question = ''
        Question = ['Question']
        Answers = ['Answers']
        S_starttime = ['S_starttime']
        S_endtime = ['S_endtime']
        with open('transcript data clean/{}_TRANSCRIPT.csv'.format(357),'r',encoding='utf-8') as f1:
            next(f1)
            f_w1 = csv.reader(f1)
            endtime = 1
            for row1 in f_w1:
                if len(row1)==0 : continue
                line = row1[0].split('\t')
                #print(line)
                    #print(ans)
                if line[3].strip().startswith('<sync') or line[3].strip().startswith('hi'): continue
                #starttime = 0
                if line[2]=='Ellie':
                    starttime = 0
                    if endtime ==0:
                        endtime = line[0]
                        S_endtime.append(endtime)
                    if ans != '':
                        Answers.append(ans)
                        print(ans)
                        ans = ''
                    question = question + ' '+line[3].strip()+'. '
                if line[2]=='Participant':
                    endtime = 0
                    if starttime ==0:
                        starttime = line[0]
                        S_starttime.append(starttime)
                    if question !='':
                        Question.append(question)
                        print(question)
                        question = ''
                    ans = ans+ ' ' +line[3].strip()+'. '
        #print(len(Question),len(Answers))
        #print(Question)
        #print(Answers)
        print(len(S_endtime),len(S_starttime),len(Answers))
        if len(Answers)>len(Question): min = len(Question)
        else: min = len(Answers)
        id = ['id']
        print(row[0],bi,score)
        for i in range(1,min):
            id.append(row[0])
            label_binary.append(bi)
            label_continue.append(score)
            gender.append(row[3])
        print(row[0],bi,score)
        with open('Q&A/{}_Q&A.csv'.format(357),'w',encoding='utf-8',newline='') as f2:
            f_w2 = csv.writer(f2)
            for i in range(min):
                row2 =[id[i],label_binary[i],label_continue[i],gender[i],S_starttime[i],S_endtime[i],Question[i],Answers[i]]
                f_w2.writerow(row2)





