def lastOccurrence(array, toFind):
    if(not len(array)):
        return -1
    lastIndex = lastOccurrence(array[1:], toFind)
    if(lastIndex != -1):
        return lastIndex + 1
    else:
        if(array[0] == toFind):
            return 0
        else:
            return -1


print(lastOccurrence([1, 2, 3, 4, 5, 1], 1))
