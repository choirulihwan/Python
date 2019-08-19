from functools import reduce
#without reduce
listItems = [1,2,3,4,5,6,7]
print(listItems)
sum = 0
for item in listItems:
    sum = sum + item
print(sum)

#with reduce
sum2 = reduce(lambda x,y:x+y, listItems)
print(sum2)