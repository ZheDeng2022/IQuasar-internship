import numpy as np
import pandas as pd
import csv

parsed = pd.read_csv('parsed.csv') 
diabetes,heart,cancer,ahlzeimers,melanoma,hiv = [],[],[],[],[],[]
for j in list(set(parsed['article-title'].tolist())):
    if 'diabetes' in j: diabetes.append(j)
    elif 'heart' in j: heart.append(j)
    elif 'cancer' in j: cancer.append(j)
    elif "ahlzeimer's" in j: ahlzeimers.append(j)
    elif 'melanoma' in j: melanoma.append(j)
    elif 'hIV' in j: hiv.append(j)
clinical = pd.read_csv('clinical.csv') 
head = ['Clinical Trial', '# of related articles']
with open("jointData.csv","w") as h:
    writer = csv.writer(h)
    writer.writerow(head)
    for k in list(set(clinical['Title'].tolist())):
        row=[]
        if 'Diabetes' in k: 
            row.append(k)
            row.append(len(diabetes))
            writer.writerow(row)
        elif 'Heart' in j: 
            row.append(k)
            row.append(len(heart))
            writer.writerow(row)
        elif 'Cancer' in j:
            row.append(k)
            row.append(len(cancer))
            writer.writerow(row)
        elif "Ahlzeimer's" in j: 
            row.append(k)
            row.append(len(ahlzeimers))
            writer.writerow(row)
        elif 'Melanoma' in j: 
            row.append(k)
            row.append(len(melanoma))
            writer.writerow(row)
        elif 'HIV' in j: 
            row.append(k)
            row.append(len(hiv))
            writer.writerow(row)