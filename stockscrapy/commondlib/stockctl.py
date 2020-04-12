# -*- coding:utf-8 -*-
import os
import sys
import chardet
stock_no=[]
allstockdict={}
def readallstock(filepath):
    filepath=os.path.join(os.getcwd(),"data","allstock.csv")
    print(filepath)
    with open(filepath, 'r+') as csv_file:
        for line in csv_file:
            no =line.split(",")[0].zfill(6)
            stock_no.append(no)
            name =line.split(",")[1].replace('\n',"")
           
            allstockdict[no]=name
			#print "%s:%s"%(no,str(allstockdict[no]))
    return allstockdict
if __name__ == "__main__":
    get_input = sys.argv
    name  = get_input[1]
    readallstock(name)
