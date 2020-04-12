# -*- coding:utf-8 -*-
def writetofile(filepath,content):
	f=open(filepath,"a+")
	f.write(content)
	f.close()
if __name__=="__main__":
	print "commondlib main start"
