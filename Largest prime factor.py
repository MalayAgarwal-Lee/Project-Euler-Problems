from math import sqrt

'''
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

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
    number = 600851475143
    print(max(getPrimeFactors(number)))

if __name__ == '__main__':
    main()