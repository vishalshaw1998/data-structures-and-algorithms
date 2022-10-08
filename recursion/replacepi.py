# Replace "pi" in a string with "3.14"

def replacePi(string):
    if(len(string) < 2):
        return string
    if(len(string) == 2 and string[0] != 'p' and string[1] != 'i'):
        return string
    replacedString = replacePi(string[1:])
    if(string[0] == 'p' and replacedString[0] == 'i'):
        return '3.14' + replacedString[1:]
    else:
        return string[0] + replacedString


print(replacePi("csppisacpi"))
