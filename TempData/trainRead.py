from itertools import chain
import nltk
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import LabelBinarizer
import sklearn

import nltk
import pandas as pd
sent=[]
a=pd.read_csv('t11', sep=" ", header = None) 

all_words=a.as_matrix()
import nltk.tag.stanford as st
PATH_TO_GZ = 'C:/Users/Oma/Desktop/Desktop/Fall 2016/NLP/project/tagset/tagger-master/dataset/stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz'
PATH_TO_JAR = 'C:/Users/Oma/Desktop/Desktop/Fall 2016/NLP/project/tagset/tagger-master/dataset/stanford-ner/stanford-ner.jar'
tagger = st.StanfordNERTagger(PATH_TO_GZ, PATH_TO_JAR) 

sent=[]
train_sents=[]

for i in range(0,100):
    #print(i)
    if(all_words[i][0]=='end_of_sentence'):
        train_sents.append(list(sent))
        sent=[]
    else:
        sent.append(all_words[i])
print("COmplete stage1")
