#coding:utf-8
import csv
import re
question = []
with open('0ques_statistic_temp.csv','r',encoding='utf-8') as r:
    r_t = csv.reader(r)
    for row in r_t:
        if int(row[0])>68:
            question.append(row[1])
commonquestion = []
sentencenumber = []
for ele in question:
    commonquestion.append(ele)
    s = 0
    num = 0
    with open('0ques_statistic.csv','r',encoding='utf-8') as r:
        next(r)
        r_t = csv.reader(r)
        for row in r_t:
            print(ele.lower(),row[1])
            if re.sub('\.','',ele.lower()) in row[1]:
                s = s + int(row[2])
                num = num + 1
    sentencenumber.append(s/num)

with open('0ques_statistic_temp1.csv','w',encoding='utf-8',newline='') as w:
    w_t = csv.writer(w)
    for i in range(len(commonquestion)):
        row_in =[commonquestion[i],sentencenumber[i]]
        w_t.writerow(row_in)



