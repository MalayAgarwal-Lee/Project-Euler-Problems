from math import sqrt
from collections import Counter
from functools import reduce


def generateTriangularNumbers():

    n = 7

    while True:

        num = (n * (n + 1))/2
        yield int(num) if num % 2 == 0 else 0
        n += 1


def generatePrimeNumbers():

    number  = 2
    c = 0

    while True:

        if not (number % 2 == 0 and number > 2):

            for divisor in range(3, int(sqrt(number))+1, 2):

                if number % divisor == 0:
                    c = 1
                    break

            if  c != 1:
                yield number

        number += 1
        c = 0



def primeFactorizeNumber(currentNumber):
    primeNumbers = generatePrimeNumbers()
    output = []

    while currentNumber > 1:

        factor = next(primeNumbers)

        if currentNumber % factor == 0:
            output.append(factor)
            currentNumber /= factor
            primeNumbers = generatePrimeNumbers()

        else:
            continue

    return output



def main():

    c = True
    triangularNumbers = generateTriangularNumbers()
    while c:

        currentNumber = next(triangularNumbers)
        if currentNumber != 0:
            powerCount = list(Counter(primeFactorizeNumber(currentNumber)).values())
            numberOfFactors = reduce(lambda x, y: x * y, map(lambda x: x + 1, powerCount))

            if numberOfFactors > 500:
                print(currentNumber)
                c = False

main()