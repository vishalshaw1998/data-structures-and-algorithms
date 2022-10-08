def firstOccurrence(string, char, index=0):
    if(index == len(string)):
        return -1
    if(string[index] == char):
        return index
    return firstOccurrence(string, char, index+1)


print(firstOccurrence("abcd", "e"))
