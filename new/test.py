
print('code start')
import os 
import time
from collections import Counter
import shutil

#get files of current dir
#extract date of file 
#mak path lik month/day depend on file date
#move file to its new dir 

#get current folder of the code file
cwd = os.getcwd()
print(cwd)

#get file and its creation date
def getFilesDatesInTheCurrentDir():
    filesDis=[]
    filesDate=[]
    fileAndDate={}
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for f in files:
            print(time.ctime(os.path.getctime(f)))
            # my_files.append()
            filesDate.append(time.ctime(os.path.getctime(f)))
            filesDis.append(f)
    res = {filesDis[i]: filesDate[i] for i in range(len(filesDis))}        
    return res


def makDirIfNotExeist(dirName,subdirName):
    if not os.path.exists(dirName):
        os.makedirs(os.path.join(dirName,subdirName))
    else:print('the folder already exist')
        

my_files=[]





# def makeDirByMonth():
#     fileList=getFilesInTheCurrentDir()
#     for f in fileList:
#         month=f.split()[1]
#         # os.makedirs(time.ctime(os.path.getctime(f)).split()[1])
#         makDirIfNotExeist(month)
 
# def makeDirByDay():
#         fileList=getFilesInTheCurrentDir()
#         for f in fileList:
#             month='{}o{}'.format(f.split()[2],f.split()[3]) 
#             # os.makedirs(time.ctime(os.path.getctime(f)).split()[1])
#             makDirIfNotExeist(month)
def makeDirByDay():
        fileList=getFilesDatesInTheCurrentDir()
        for f in fileList:
            month= f.split()[1] 
            day=f.split()[2]
            newPath=month+day
            makDirIfNotExeist(month,day)
            #move file ot the new path
            shutil.move("\\{}", '.{}{}'.format(f,'\\',newPath))

def makDateTree():
    #create monthes folder 
    #create days folders inside monthes folders
    #move each file to its month-day folder
    return null
#path = f.split('.')[2]+'/'+f.split('.')
def groupFiles():

    for f in getFilesInTheCurrentDir():
        month=f.split('.')[1]
        day=f.split('.')[2]
        dest='{}/{}'.format(month,day)
        shutil.move(f, dest)
         


if __name__ == '__main__':
    # g='{}/{}'.format('sep','2')
    # print(g)
    # makeDirByDay()
    print(getFilesDatesInTheCurrentDir())

  

#get duplicated elements 
# print([key for key in Counter(my_files).keys() if Counter(my_files)[key]>1])

