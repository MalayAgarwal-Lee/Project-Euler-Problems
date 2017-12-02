from math import sqrt
from functools import reduce
from time import time

'''
Problem 35
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''


def isPrime(number):

    if not (number > 2 and number % 2 == 0):

        for divisor in range(3, int(sqrt(number)) + 1, 2):
            if number % divisor == 0:
                return False

        return True

    else:
        return False

def listCheck(l):

    for number in l:
        if not isPrime(number):
            return False
    return True

def generateCircularPermutations(l):

    number = 1
    circularPerms = []
    circularPerms.append(l)
    length = len(l)
    l2 = l.copy()
    while number < length:
        for i in range(0, length - 1):
            l2[i], l2[i + 1] = l2[i + 1], l2[i]

        circularPerms.append(l2)
        number += 1
        l2 = l2.copy()

    return list(map(lambda per: reduce(lambda x, y: int(x) * 10 + int(y), per), circularPerms))


def filterPrimes():

    sieve = {2: False}
    sieve.update({i: False for i in range(3, 1000001, 2)})

    for k in list(sieve.keys())[1:]:

        if not sieve[k]:
            for i in range(k**2, 1000001, 2):
                if i % k == 0:
                    sieve[i] = True

    return list(filter(lambda x: sieve[x] == False, sieve.keys()))


def main():
    start = time()
    primes = filterPrimes()
    count = 13
    for prime in primes[25:]:
        rotations = generateCircularPermutations(list(str(prime)))

        if listCheck(rotations):
            count += 1

    print(count)
    print(time() - start)


if __name__ == '__main__':
    main()
