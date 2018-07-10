# coding: utf-8
__author__ ='Guohou Shan'

import csv


for i in range(300,493):
    start_time = ['start_time']
    end_time = ['end_time']
    who = ['who']
    content =['content']
    len_time = ['len_time']
    try:
        with open('transcript data clean/{}_TRANSCRIPT.CSV'.format(i),'r',encoding='utf-8') as f:
            f_w = csv.reader(f)
            next(f_w)
            for row in f_w:
                if len(row)==0: continue
                if row[0].split('\t')[3] == '': continue
                print(row[0].split('\t')[0],row[0].split('\t')[1],row[0].split('\t')[2],row[0].split('\t')[3])
                start_time.append(row[0].split('\t')[0])
                end_time.append(row[0].split('\t')[1])
                who.append(row[0].split('\t')[2])
                content.append(row[0].split('\t')[3])
                len_time.append(float(row[0].split('\t')[1])-float(row[0].split('\t')[0]))

        with open('transcript data clean/{}_participant.CSV'.format(i),'w',encoding='utf-8',newline='') as f:
            f_w = csv.writer(f)
            for i in range(len(start_time)):
                if who[i] == 'Ellie': continue
                row = [start_time[i],end_time[i],len_time[i],who[i],content[i]]
                f_w.writerow(row)
    except (IOError): print('no file')
    else: continue
