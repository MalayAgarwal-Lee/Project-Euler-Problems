from functools import reduce
from math import sqrt

'''
Problem 47
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?


'''


def isPrime(number):

    if not (number > 2 and number % 2 == 0):

        for i in range(3, int(sqrt(number)) + 1, 2):
            if number % i == 0:
                return False

        return True

    else:
        return False

def generatePrimeNumbers():

    number  = 2
    c = 0

    while True:

        if isPrime(number):
            yield number

        number += 1
        c = 0


def getPrimeFactors(multiple):

    primeNumbers = generatePrimeNumbers()
    output = []

    while multiple > 1:

        factor = next(primeNumbers)

        if multiple % factor == 0:
            output.append(factor)
            multiple /= factor
            primeNumbers = generatePrimeNumbers()

        else:
            continue

    return output

def main():
    n = 10000
    requiredNumber = 0
    while True:
        c = 0

        if not isPrime(n):

            primeFactors = set(getPrimeFactors(n))

            if len(primeFactors) == 4:

                for i in range(n + 1, n + 4):
                    if not isPrime(i):
                        length = len(set(getPrimeFactors(i)))

                        if length != 4:
                            c = 1
                            break
                    else:
                        c = 1
                        break

                if c != 1:
                    requiredNumber = n
                    break

        n += 1

    print(requiredNumber, primeFactors)


if __name__ == '__main__':
    main()