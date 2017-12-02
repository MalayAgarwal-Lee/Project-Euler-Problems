from math import sqrt
from functools import reduce


def getSieve():

    sieve = {i: False for i in range(1009, 10000) if i % 2 != 0}
    for key in sieve.keys():
        for i in range(3, int(sqrt(key)) + 1, 2):
            if key % i == 0:
                sieve[key] = True
                break

    primeNumbers = list(map(str, filter(lambda x: sieve[x] == False, sieve.keys())))
    primeNumbers.remove("1487")
    return primeNumbers

if __name__ == '__main__':

    primeNumbers = getSieve()
    length = len(primeNumbers)
    firstNum = 0
    secondNum = 0
    thirdNum = 0
    for i in range(0, length):

        firstDigitList = list(primeNumbers[i])
        tempFirstDigitList = list(primeNumbers[i])
        tempFirstDigitList.sort()
        c = 0
        for j in range(i + 1, length):
            thirdDigitList = list(primeNumbers[j])
            tempThirdDigitList = list(primeNumbers[j])
            tempThirdDigitList.sort()

            if tempThirdDigitList == tempFirstDigitList:
                firstNum = reduce(lambda x, y: int(x)*10 + int(y), firstDigitList)
                thirdNum = reduce(lambda x, y: int(x)*10 + int(y), thirdDigitList)
                secondNum = (firstNum + thirdNum)//2

                if str(secondNum) in primeNumbers:

                    secondDigitList = list(str(secondNum))
                    secondDigitList.sort()
                    if secondDigitList == tempFirstDigitList:
                        print(firstNum)
                        print(secondNum)
                        print(thirdNum)
                        c = 1
                        break
        if c == 1:
            break


    print(str(firstNum) + str(secondNum) + str(thirdNum))