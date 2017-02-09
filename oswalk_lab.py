##using os.walk to recursively walk directory tree

import os

'''
rootDir = '.' #current Directory
for dirName, subdirList, fileList in os.walk(rootDir):
    print ('Found directory: %s' % dirName)
    for fname in fileList:
        print('\t%s' % fname)
'''



#using os.walk to find all the files with the extention
for root, dirs, files in os.walk("."):
    for name in files:
        if(name.lower().endswith(".py")):
            print(os.path.join(root,name))
