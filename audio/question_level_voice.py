#coding:utf-8
import csv
# feature 1-74 定义 f0-f73
var = locals()
varl = locals()

id = ['id']
label_binary = ['PHQ-8_binary']  # >10 is 1 or 0
label_continue = ['PHQ-8_score']
gender = ['gender']

with open('prepared_dataset_questionlevel.csv','r',encoding='utf=8') as f:
    next(f)
    f_w = csv.reader(f)
    #for i in range(74):
     #   name = 'f'+str(i)
      #  varl['f'+str(i)]=['f{}'.format(i)]
        #print(type(varl['f'+str(i)]))
    #用list套list取代多变量定义问题
    feature = []
    for i in range(74):
        feature.append(['f'+'{}'.format(i)])
    for row in f_w:

        id.append(row[0])
        label_binary.append(row[1])
        label_continue.append(row[2])
        gender.append(row[3])
        start = int(float(row[4])*100)
        end = int(float(row[5])*100)
        total = end-start+1
        tag = 0
        with open('audio data/{}_COVAREP.csv'.format(row[0]),'r',encoding='utf-8') as f1:
            f_w1 = csv.reader(f1)
            count = 0
            tag = tag + 1
            #if tag <5: continue
            print(row[0])
            for i in range(74):
                name = 's'+str(i)
                var['s'+str(i)]= 0
            for row1 in f_w1:
                count = count + 1
                if count<start or count>end: continue
                for i in range(74):
                    var['s'+str(i)] = var['s'+str(i)] + float(row1[i])
        for i in range(74):
            value = var['s'+str(i)]/total
            feature[i].append(value)

for i in range(74):
    print(len(feature[i]))
print(len(id),len(label_continue),len(label_binary),len(gender))

with open('audio_question_level.csv','w',encoding='utf-8',newline='') as f2:
    f_w2 = csv.writer(f2)
    for i in range(len(id)):
        row = [id[i],label_binary[i],label_continue[i],gender[i]]
        for j in range(74):
            row.append(feature[j][i])
        f_w2.writerow(row)
