# -*- coding:utf-8 -*-
import os
import sys
import chardet
stock_no=[]
allstockdict={}
def readallstock(filepath):
    filepath=os.path.join(os.getcwd(),"data","allstock.csv")
    with open(filepath, 'r+') as csv_file:
        for line in csv_file:
            no =line.split(",")[0].split(".")[0].zfill(6)
            stock_no.append(no)
            name =line.split(",")[1].replace('\n',"")
            #nameutf = name.decode("gbk").encode("utf-8")
            allstockdict[no]=name
			#print "%s:%s"%(no,str(allstockdict[no]))
    return allstockdict
def readallstockid(filepath):
    filepath=os.path.join(os.getcwd(),"data","allstock.csv")
    with open(filepath, 'r+') as csv_file:
        for line in csv_file:
            no =line.split(",")[0].zfill(6)
            stock_no.append(no)
            allstockdict[no]=no
			#print "%s:%s"%(no,str(allstockdict[no]))
    return allstockdict
