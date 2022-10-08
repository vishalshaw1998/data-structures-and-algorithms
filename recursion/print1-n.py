def print1ToN(number, init=1):
    print(init)
    if(init == number):
        return
    print1ToN(number, init + 1)


print1ToN(5)
