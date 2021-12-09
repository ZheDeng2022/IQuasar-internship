import numpy as np
import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import xml.etree.ElementTree as ET


def score(arr,article):
    score=0
    for i in arr:
        if article != i:
            score+=fuzz.ratio(article,i)
    return score/(len(arr)-1)
clinical = pd.read_csv('clinical.csv')

diabetes,heart,cancer,ahlzeimers,melanoma,hiv = [],[],[],[],[],[]
for j in list(set(clinical['Title'].tolist())):
    if 'Diabetes' in j: diabetes.append(j)
    elif 'Heart' in j: heart.append(j)
    elif 'Cancer' in j: cancer.append(j)
    elif "Ahlzeimer's" in j: ahlzeimers.append(j)
    elif 'Melanoma' in j: melanoma.append(j)
    elif 'HIV' in j: hiv.append(j)

idx=[]
topic=[]
simScore=[]
for i in list(set(clinical['Title'].tolist())):
    if i in diabetes:
        idx.append(i)
        topic.append('Diabetes')
        simScore.append(score(diabetes,i))
    elif i in heart:
        idx.append(i)
        topic.append('Heart')
        simScore.append(score(heart,i))
    elif i in cancer:
        idx.append(i)
        topic.append('Cancer')
        simScore.append(score(cancer,i))
    elif i in ahlzeimers:
        idx.append(i)
        topic.append("Ahlzeimer's")
        simScore.append(score(ahlzeimers,i))
    elif i in melanoma:
        idx.append(i)
        topic.append('Melanoma')
        simScore.append(score(melanoma,i))
    elif i in hiv:
        idx.append(i)
        topic.append('HIV')
        simScore.append(score(hiv,i))
inference = pd.DataFrame(index=idx,columns=['Topic','Similarity Score'])
inference['Topic']=topic
inference['Similarity Score']=simScore
print(inference)