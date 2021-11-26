import sys
import csv
import numpy as np
import pandas as pd
import xml.etree.ElementTree as ET
import os

dirNum = "";
dirName = "files/NCT000"+str(dirNum)+"xxxx"

head = ["Title","Facility","City","State","Zip","Country"]

with open("clinical.csv","w") as h:
    writer = csv.writer(h)
    writer.writerow(head)
    for i in range(0,513):
        dirNum = str(i).zfill(4)
        dirName = "files/NCT"+dirNum+"xxxx" 
        xml = os.listdir(dirName)
        for f in xml:
            tree = ET.parse(dirName+"/"+f)
            root = tree.getroot()
            for k in root.iter('facility'):
                row=[]
                row.append(root.find('./brief_title').text)
                try: row.append(k.find("./name").text)
                except AttributeError: row.append("N/A")
                try: row.append(k.find("./address/city").text)
                except AttributeError: row.append("N/A")
                try: row.append(k.find("./address/state").text) 
                except AttributeError: row.append("N/A")
                try: row.append(k.find("./address/zip").text)
                except AttributeError: row.append("N/A")
                try: row.append(k.find("./address/country").text)
                except AttributeError: row.append("N/A")
                writer.writerow(row)