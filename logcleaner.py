#!/bin/python3
# $logcleanre.py 10 7

import shutil
import os
import sys

if(len(sys.argv)<4): #количество аргументов, переданных скрипту через параметры командной строки
    print("Missing arguments! Use logcleaner 10 7")
    exit(1)
fileName=sys.argv[1]
limitSize=int(sys.argv[2])
logsNumber=int(sys.argv[3])

#проверка на существование самого файла с логами, который указан в параметрах скрипта
if(os.path.isfile(fileName)==True):
    logFileSize=os.stat(fileName).st_size #File size in bytes
    logFileSize=logFileSize/1024 #File size recalculate in Kb
    if(logFileSize>=limitSize):
        if(logsNumber>0):
            for currentFileNum in range(logsNumber,1,-1):
                src=fileName+"_"+str(currentFileNum-1)
                dst=fileName+"_"+str(currentFileNum)
                if(os.path.isfile(src)==True):
                    shutil.copyfile(src,dst)
                    print("Copied: "+src+" to "+dst)

            shutil.copyfile(fileName,fileName+"_1")
            print("Copied: "+fileName+" to "+fileName+"_1")
        myfile=open(fileName,'w')
        myfile.close()