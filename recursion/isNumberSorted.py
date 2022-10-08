def checkIfNumberSorted(array):
    if(len(array) == 1):
        return True
    if(array[0] < array[1] or array[0] == array[1]):
        return checkIfNumberSorted(array[1:])
    else:
        return False


print(checkIfNumberSorted([1]))
