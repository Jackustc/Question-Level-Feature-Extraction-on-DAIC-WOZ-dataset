#coding:utf-8
import csv
import pandas as pd
question = []
with open('0ques_statistic.csv','r',encoding='utf-8') as r:
    next(r)
    r_t = csv.reader(r)
    for row in r_t:
        #count = 0
        question_temp=row[1].strip().split('.')
        if len(question_temp)==2:
            question.append(question_temp[0])
        else: question.append(question_temp[1])
print(len(question))
question_no = set(question)
time = []
question_con = []
for item in question_no:
    print(item,question.count(item))
    time.append(question.count(item))
    question_con.append(item)
with open('0ques_statistic_temp.csv','w',encoding='utf-8',newline='') as w:
    w_t = csv.writer(w)
    for i in range(len(time)):
        row_in =[time[i],question_con[i]]
        w_t.writerow(row_in)

