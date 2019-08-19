listItems = [1,2,3,4,5,6,7]
print(listItems)

#without map
tempList = []
for item in listItems:
    tempList.append(item*2)
print(tempList)

#with map
tempList2 = list(map(lambda x:x*2, listItems))
print(tempList2)