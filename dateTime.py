import re

date1 = "10/30/2021"
date2 = "March 24, 2021"

class Date:
    monthToNum = {'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,
        'July':7,'August':8,'September':9,'October':10,'November':11,'December':12}
    numToMonth = {v: k for k, v in monthToNum.items()}
    def __init__(self, date,form):
        self.form = form
        if form:
            self.date = list(map(int,date.split("/")))
        else:
            self.date = re.split(" |, ",date)
            self.date[0] = Date.monthToNum[self.date[0]]
            self.date = list(map(int,self.date))
        

    def getMonth(self):  return self.date[0]
    def getDay(self):  return self.date[1]
    def getYear(self):  return self.date[2]

    def setMonth(self, month):
        self.date[0]=month
    def setDay(self, day):
        self.date[1]=day
    def setYear(self, year):
        self.date[2]=year
    def toString(self):
        print("Month: "+str(self.getMonth())+", Day: "+str(self.getDay())+", Year: "+str(self.getYear()))

date = Date(date2, False)
date.toString()

    
    

    
