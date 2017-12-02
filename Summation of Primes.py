from functools import reduce
from math import sqrt

def generatePrimeNumbers():

    number  = 2
    c = 0

    while number < 2000000:

        if not (number % 2 == 0 and number > 2):

            for divisor in range(3, int(sqrt(number))+1, 2):

                if number % divisor == 0:
                    c = 1
                    break

            if  c != 1:
                yield number

        number += 1
        c = 0


def main():

    summation = reduce(lambda x, y: x + y, generatePrimeNumbers())
    print(summation)

main()