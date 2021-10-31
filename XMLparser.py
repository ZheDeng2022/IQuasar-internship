import sys
import csv
import numpy as np
import pandas as pd
import defusedxml.ElementTree as ET

fileName = "pmc_result-2.xml"

try:
    tree = ET.parse(fileName)

except FileNotFoundError:
    print(f"File not found: {fileName}")
    sys.exit(1)

refs = {'publication-type' : [],'article-title' : [], 'author' : [], 'source' : [], 'year' : []}
for i in tree.findall('./article/back/ref-list/ref/element-citation'):
    refs['publication-type'].append(i.attrib['publication-type'])
    refs['article-title'].append(i.find('./article-title').text)
    refs['source'].append(i.find('./source').text)
    refs['year'].append(i.find('./year').text)
    #refs['volume'].append(i.find('./volume').text)
    #refs['pub-id'].append(i.find('./pub-id[@pub-id-type="pmid"]').text)


header = ['publication-type', 'article-title', 'source', 'year']

with open('parsed.csv','w') as f:
    writer = csv.writer(f)

    writer.writerow(header)

    for i in range(len(refs['publication-type'])):
        writer.writerow([refs['publication-type'][i], refs['article-title'][i],refs['source'][i],refs['year'][i]])


referencesDF = pd.read_csv('parsed.csv')

print(referencesDF)