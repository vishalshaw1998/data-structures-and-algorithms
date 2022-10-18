def binarySearch(array, left, right, toFind):
    if(left > right):
        return -1
    middleIndex = (left+right) // 2
    middleElement = array[middleIndex]
    if(middleElement == toFind):
        return middleIndex
    elif(middleElement > toFind):
        return binarySearch(array, left, middleIndex-1, toFind)
    else:
        return binarySearch(array, middleIndex+1, right, toFind)


print(binarySearch([1, 2, 3, 4, 5, 6, 7, 8], 0, 7, 4))
