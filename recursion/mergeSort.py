def merge(leftList, rightList):
    sortedList = []
    i = 0
    j = 0
    while(i < len(leftList) and j < len(rightList)):
        if(leftList[i] <= rightList[j]):
            sortedList.append(leftList[i])
            i += 1
        else:
            sortedList.append(rightList[j])
            j += 1
    while(i < len(leftList)):
        sortedList.append(leftList[i])
        i += 1
    while(j < len(rightList)):
        sortedList.append(rightList[j])
        j += 1
    return sortedList


def mergeSort(list):
    if(len(list) == 1 or len(list) == 0):
        return list
    middle = len(list) // 2
    sortedLeft = mergeSort(list[0:middle])
    sortedRight = mergeSort(list[middle:])
    mergedSortedList = merge(sortedLeft, sortedRight)
    return mergedSortedList


print(mergeSort([21, 31321, 4321, 3112, 131, 423, 1214, 113, 4245, 435, 343]))
