def sumOfNaturalNumber(number):
    if(number == 1):
        return 1
    return number + sumOfNaturalNumber(number - 1)


print(sumOfNaturalNumber(3))
