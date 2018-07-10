#coding:utf-8
#instruction: question and answer summary
import csv
import os
import re

id = ['id']
ques = ['question']
ans_sentence_count = ['ans_sentence_count']

path = 'E:/SELF Learning/2018规划/data/depression dataset/depression dataset/Q&A'
question = []
files= os.listdir(path)
for file in files:
    with open('Q&A/{}'.format(file),'r',encoding='utf-8') as f:
        next(f)
        f_t = csv.reader(f)
        number = 0
        for row in f_t:
            question = re.findall(r'where.+\.|how.+\.|why.+\.|are.+\.|what.+\.|do.+\.|has.+\.|who.+\.|'
r'can.+\.|tell.+\.|whatever.+\.|could.+\.|when.+\.|have.+\.',row[6])
            if len(question)>0:
                ans_num = 0
                number = number + 1
                for ele in row[7].strip().split('.'):
                    if ele !='': ans_num = ans_num+1
                id.append(row[0])
                ques.append(question[0])
                ans_sentence_count.append(ans_num)
with open('0ques_statistic.csv','w',encoding='utf-8',newline='') as w:
    w_t = csv.writer(w)
    for i in range(len(id)):
        row_in =[id[i],ques[i],ans_sentence_count[i]]
        w_t.writerow(row_in)
