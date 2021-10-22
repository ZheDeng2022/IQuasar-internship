import csv
import requests
import xml.etree.ElementTree as ET
  
def loadXML():

    url = 'https://jats.nlm.nih.gov/publishing/tag-library/1.0/FullArticleSamples/pnas_sample.txt'
  
    resp = requests.get(url)
  
 
    with open('/Users/swapna.velleleth/IQuasar/nihArticle.xml', 'wb') as f:
        f.write(resp.content)
          
def parseXML(xmlfile):
  
    tree = ET.parse(xmlfile)

    root = tree.getroot()
  
    authorNames = []
  

    for item in root.findall('./front/article-meta/contrib-group/contrib/name/surname'):
        print(item.text)
      
   
  
  
def savetoCSV():
    pass
      
#loadXML()

parseXML('nihArticle.xml')

      
