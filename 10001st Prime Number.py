from math import sqrt

def generatePrimeNumbers():

    number  = 19
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



def main():

    i = 8
    primeNumbers = generatePrimeNumbers()
    number = 0
    while i <= 100001:
        number = next(primeNumbers)
        i += 1
    print(number)

main()
