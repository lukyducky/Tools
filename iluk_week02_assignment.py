#bella luk; week 02 HW

#question 01: flatten into a single list

L = [["a","b","c",[100,200,300]],"polyCube",["polySphere", [10,20,30]]]


#sum(iterable, [,start]) <- where the iterable is of things we can sum/add together,
#and the second [] is what is added to the sum of the iterable
#isInstance(a, b) -> is a in instance/of the type of b?

def flatten(inList):
    return sum(([item] #iterable -> is a list!  and 
                if not isinstance(item, list) #checks if each item in list is not a list;
                #recursive
                else flatten(item) for item in inList), [] ) #if it is a list, run the function again 

print "Flattening list = ", flatten(L)





#question 02: write a script or function that can traverse a given subdirectory and
#rename all the file found in the subdirectory by adding 


import os
import sys
import shutil

def rename(dirName):
    #getting full paths
    mypath = os.path.abspath(dirName)
    sys.path.append(mypath) #adding to syspath so python can find it
    
    for name in os.listdir(dirName):
        newname = "old_" + name
        #getting full paths
        name = os.path.join(mypath, name)
        newname = os.path.join(mypath, newname)
        print('Renaming "%s" to "%s" ...'% (name, newname))
        shutil.move(name, newname)

rename(r"D:\SCHOOL\ACTUAL SP-17\Tools\aFolder") #using r"string" format to stop the \safe chara thing



        
