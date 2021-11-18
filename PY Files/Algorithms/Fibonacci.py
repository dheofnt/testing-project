def fibonacci (num) :
    theList = []
    for i in range(num) :
        if(i < 2) :
            theList.append(1)
        else :
            theList.append(theList[i-1] + theList[i-2])
    return theList


for i in range(1, 10):
    print(fibonacci(i))
