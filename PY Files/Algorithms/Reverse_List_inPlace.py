import math

def reverseList(theList):
    panjangList = len(theList)
    for i in range(math.floor(panjangList/2)) :
        theList[i], theList[panjangList - 1 - i] = theList[panjangList - 1 - i], theList[i]

    return theList

list1 = [True]
list2 = ['andi', 'budi', 'leli', 'dedi', 'ceci']
list3 = [1,2,3,4,5,6]

reverseList(list1)
reverseList(list2)
reverseList(list3)

print(list1)
print(list2)
print(list3)

print(reverseList([True, False]))
print(reverseList(['andi', 'budi', 'leli', 'dedi', 'ceci']))
print(reverseList([1,2,3,4,5,6]))

# OR
###########################################################
# OR


capitals = ['Oslo', 'Skopje', 'Riga', 'Madrid']

capitals.reverse()

print('Reversed list:', capitals)