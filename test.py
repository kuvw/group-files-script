
print('code start')
import os 
import time
from collections import Counter


cwd = os.getcwd()
print(cwd)
# for root,dirs,files in os.walk(cwd):
#     # print('looking in ',root)
#     for Files in files:
#         try:
#             # print(os.stat(Files))
#             stats=os.stat(Files)
#             print(stats.st_atime)
#         except:
#             exit()

# dirlist=os.listdir(cwd)
def makDirIfNotExeist(dirName):
    if not os.path.exists(dirName):
        os.makedirs(dirName)
    else:print('the folder already exist')
        

my_files=[]

def getFilesInTheCurrentDir():
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for f in files:
            print(time.ctime(os.path.getctime(f)))
            my_files.append(time.ctime(os.path.getctime(f)))
    return my_files



def makeDirByMonth():
    fileList=getFilesInTheCurrentDir()
    for f in fileList:
        month=f.split()[1]
        # os.makedirs(time.ctime(os.path.getctime(f)).split()[1])
        makDirIfNotExeist(month)
 
def makeDirByDay():
        fileList=getFilesInTheCurrentDir()
        for f in fileList:
            month=f.split()[2]
            # os.makedirs(time.ctime(os.path.getctime(f)).split()[1])
            makDirIfNotExeist(month)

def makDateTree():
    #create monthes folder 
    #create days folders inside monthes folders
    #move each file to its month-day folder
    return null
if __name__ == '__main__':
    makeDirByDay()

  

#get duplicated elements 
# print([key for key in Counter(my_files).keys() if Counter(my_files)[key]>1])

