#coding:utf-8
import csv
f = []
content  = []
id = '0'
s = 1
with open('audio.csv','r',encoding='utf-8') as r:
    for line in r.readlines():
        row = line.split(',')
        if id != row[0]:
            for i in range(len(f)):
                if type(f[i]) is not str: f[i] =f[i]/s
            content.append(f)
            f = []
            for i in range(len(row)):
                f.append(row[i].strip())
            s = 1
        else:
            s = s+1
            for i in range(len(row)):
                f[i]=float(f[i])+float(row[i])
        id = row[0]
        print(content)
with open('aduio_temp.csv','w',encoding='utf-8',newline='') as w:
    w_t = csv.writer(w)
    for i in range(1,len(content)):
        w_t.writerow(content[i])
