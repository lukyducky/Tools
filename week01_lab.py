#question 1: compute sum of all elements of list
myList = [1,2,3,4,5,6,7,8,9,10]
x = 0
for i in myList:
    x += i
print("sum of list")
print(x)

#question 2: use range built-in function to generate a list of indexes to iterate through list
shapes = ["ballShape", "plainShape", "boxShape", "torusShape"]
x = range(len(shapes))
print(x)

#question 3: find common characters in these strings
address1 = "300 South Buena Vista STree, Burbank, CA 91506"
address2 = "10 Embarcadero WEst, Oakland CA 946017"

common = []
for i in address1:
    if i in address2:
        common.append(i)
print(common)
###alternative: s3 = intersect(address1, address2)



#question 4: print every other element of the list using for loop
X = [1,2,3,4,5,6,7,8,9,10]
other = []
for i in X:
    if i%2 == 0:
        other.append(i)
print ("every other element")
print(other)

#question 5: prints all even numbers smaller than 10; greater than or equal to 0
print(range(0, 10, 2))

#question 6 : search items for things from test
items = ["first", "second", "third"]
test = ["third", 4,5,6, "first"]
common = []
for i in items:
    if i in test:
        common.append(i)
print(common)

#question 7: step through this dictionary's keys
myDictionary = {"a": 1, "b": 2, "d": 4, "f": 6, "g": 7, "o": 10}

print(myDictionary.keys())

#question 8: write a for loop that prints myDictionary's items in sorted order
###use dictionary keys and list sort methods
myKeys = myDictionary.keys()
myKeys.sort()
for i in myKeys():
    print myDictionary[i]


#question 9: create dictionary with keys from mayaObjects; correstponding values from scaleFActor
mayaObjects = ["polyCube", "polySphere", "polyPlane"]
scaleFactor = [10.5, 45.0, 100]
newDict = {}
for i in range(len(mayaObjects)):
    newDict[mayaObjects[i]] = scaleFactor[i]
print newDict
