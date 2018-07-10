# coding: utf-8
import nltk
#nltk.download('wordnet')
#nltk.download('averaged_perceptron_tagger')
#nltk.download('sentiwordnet')
from nltk.corpus import sentiwordnet as swn

def sentivalue(doc):
    JJ = 0
    PRP = 0
    R = 0
    sentences = nltk.sent_tokenize(doc)
    stokens = [nltk.word_tokenize(sent) for sent in sentences]
    taggedlist=[]
    for stoken in stokens:
        taggedlist.append(nltk.pos_tag(stoken))
        #print(nltk.pos_tag(stoken))
    wnl = nltk.WordNetLemmatizer()

    score_list=[]
    for idx,taggedsent in enumerate(taggedlist):
        #NN = 0
        #JJ = 0
        #PRP = 0
        #R = 0
        score_list.append([])
        for idx2,t in enumerate(taggedsent):
            newtag=''
            lemmatized=wnl.lemmatize(t[0])
            if t[1].startswith('NN'):
                newtag='n'
                #NN = NN+1
            elif t[1].startswith('JJ'):
                newtag='a'
                JJ = JJ + 1
            elif t[1].startswith('V'):
                newtag='v'
                #V = V + 1
            elif t[1].startswith('R'): # adv
                newtag='r'
                R = R + 1
            else:
                if t[1].startswith('PRP'): PRP = PRP+1
                newtag=''
            if(newtag!=''):
                synsets = list(swn.senti_synsets(lemmatized, newtag))
                #Getting average of all possible sentiments, as you requested
                score=0
                if(len(synsets)>0):
                    for syn in synsets:
                        score+=syn.pos_score()-syn.neg_score()
                    score_list[idx].append(score/len(synsets))

    #print(score_list)
    sentence_sentiment=[]

    for score_sent in score_list:
        if len(score_sent)==0: continue
        sentence_sentiment.append(sum([word_score for word_score in score_sent])/len(score_sent))
    #print("Sentiment for each sentence for:"+doc)
    #print(sentence_sentiment)

    num = 0
    for i in range(len(sentence_sentiment)):
        num = num +sentence_sentiment[i]
    return [num,JJ,R,PRP]
'''
if __name__ == '__main__':
    print(sentivalue('I strongly like watching TV shows!'))
'''
