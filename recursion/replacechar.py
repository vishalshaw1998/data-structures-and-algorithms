def replaceChar(string, x, y):
    if(not len(string)):
        return string
    replacedString = replaceChar(string[1:], x, y)
    if(string[0] == x):
        return y + replacedString
    else:
        return string[0] + replacedString


print(replaceChar("abcdeeee", "e", "a"))
