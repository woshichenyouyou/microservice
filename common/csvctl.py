#!/usr/bin/python
#-*- coding: UTF-8 -*-
import csv
import sys
def opencsv(filepath,isheadexist):
    filename = filepath
    data_list=[]
    # 打开文件
    with open(filename) as f:
        # 创建cvs文件读取器
        reader = csv.reader(f)
        if isheadexist:            
            # 读取第一行，这行是表头数据。
            header_row = next(reader)
        else:
            header_row = None
        # 读取第二行，这行是真正的数据。
        for row in reader:
            data_list.append(row)           
            #print("id:%s en:%s cn:%s mat:%s"%(id,en,cn,mat))    
    return header_row,data_list
def opencsv_to_json(filepath,isheadexist,header):
    filename = filepath
    data_list={}
    json_data=[]
    # 打开文件
    with open(filename) as f:
        # 创建cvs文件读取器
        reader = csv.reader(f)
        if isheadexist:            
            # 读取第一行，这行是表头数据。
            header_row = next(reader)
        else:
            header_row = None
        # 读取第二行，这行是真正的数据。
        json_row=None
        for row in reader:
            for col in header_row:
                json_row[header_row[col]]=row[col]
        json_data.append(json_row)
    return json_data

def writecsv(filepath,datalist,csvheader=[]):
    # try:
        # file=open(filepath,'w')
        # if len(csvheader) > 0:
            # for item in csvheader:
                # file.write(item)
                # file.write(",")
            # file.write("\n")
        # for items in datalist:
            # for item in items:
                # file.write(item)
                # file.write(",")
            # file.write("\n") 
    # except Exception :
        # print("write fail")
    # finally:
        # file.close();
        
    try:    
        file = open(filepath,'w')
        csv_write = csv.writer(file,dialect='excel')
        csv_write.writerow(csvheader)
        for i in datalist:
            csv_write.writerow(i)    
    except Exception :
        print("write fail")
    finally:
        file.close();   
def QuickSort(myList,start,end):
    #判断low是否小于high,如果为false,直接返回
    if start < end:
        i,j = start,end
        #设置基准数
        base = myList[i]

        while i < j:
            #如果列表后边的数,比基准数大或相等,则前移一位直到有比基准数小的数出现
            while (i < j) and (myList[j] >= base):
                j = j - 1

            #如找到,则把第j个元素赋值给第个元素i,此时表中i,j个元素相等
            myList[i] = myList[j]

            #同样的方式比较前半区
            while (i < j) and (myList[i] <= base):
                i = i + 1
            myList[j] = myList[i]
        #做完第一轮比较之后,列表被分成了两个半区,并且i=j,需要将这个数设置回base
        myList[i] = base

        #递归前后半区
        QuickSort(myList, start, i - 1)
        QuickSort(myList, j + 1, end)
    return myList
    
def csvQuickSort(myList,start,end,col):
    #判断low是否小于high,如果为false,直接返回
    if start < end:
        i,j = start,end
        #设置基准数
        
        base = myList[i]
        while i < j:
            #如果列表后边的数,比基准数大或相等,则前移一位直到有比基准数小的数出现
            # print("j is:%d"%j)
            # print(myList[j])
            # print(int(myList[j][col]))
            # print(int(base[col]))
            while (i < j) and (float(myList[j][col]) >= float(base[col])):
                j = j - 1

            #如找到,则把第j个元素赋值给第个元素i,此时表中i,j个元素相等
            myList[i] = myList[j]
            
            #同样的方式比较前半区
            while (i < j) and (float(myList[i][col]) <= float(base[col])):
                i = i + 1
            myList[j] = myList[i]
        #做完第一轮比较之后,列表被分成了两个半区,并且i=j,需要将这个数设置回base
        myList[i] = base
        #print(myList[i])
        #print("next round")
        #递归前后半区
        csvQuickSort(myList, start, i - 1,col)
        csvQuickSort(myList, j + 1, end,col)
    return myList
if __name__ == '__main__':
    get_input = sys.argv
    srcfile = get_input[1]
    desfile = get_input[2]
    sortcol = get_input[3]
    print("src file: %s"%srcfile)
    print("des file: %s"%desfile)
    print("sortcol: %s"%sortcol)
    h,d = opencsv(srcfile,False)
    print(h)
    print(d)

    print("Quick Sort: ")
    csvQuickSort(d,0,len(d)-1,int(sortcol))
    for i in d:
        print(i)
    print("write csv")
    writecsv(desfile,d,h)