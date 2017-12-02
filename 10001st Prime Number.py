from math import sqrt

'''
Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
'''

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
