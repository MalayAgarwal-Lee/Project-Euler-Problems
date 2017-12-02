from math import floor
import time

'''
Problem 23
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''

upperLimit = 20162
integers = list(map(lambda x: x, range(1, upperLimit)))

def filterPrimes():

    sieve = {2: False}
    sieve.update({i: False for i in range(3, upperLimit, 2)})

    for k in list(sieve.keys())[1:]:

        if not sieve[k]:
            for i in range(k**2, upperLimit, 2):
                if i % k == 0:
                    sieve[i] = True

    return list(filter(lambda x: sieve[x] == False, sieve.keys()))



def getAbundantNumbers():
    primes = filterPrimes()
    abundantNumbers = set()
    limit = upperLimit - 1
    for integer in integers[11:]:
        if integer not in abundantNumbers and integer not in primes:
            sumOfDivisors = sum(filter(lambda x: integer % x == 0, integers[:integer-1]))

            if sumOfDivisors > integer:
                abundantNumbers.update(set(map(lambda x: integer * x, range(1, int(floor(limit/integer)) + 1))))

    return list(abundantNumbers)


def sumOfAbundantNumbers(abundantNumbers):
    abundantSums = []
    length = len(abundantNumbers)
    limit = upperLimit - 1
    for i in range(0, length):
        abundantSums.extend(map(lambda x: abundantNumbers[i] + x if (abundantNumbers[i] + x) < limit else None, abundantNumbers[i:]))
    return set(abundantSums) - {None}


def main():
    start = time.time()
    abundantSums = sumOfAbundantNumbers(getAbundantNumbers())
    summation = sum(range(1, 24))
    nonAbundantSums = filter(lambda x: x not in abundantSums, integers[24:])
    print(summation + sum(nonAbundantSums))
    print(time.time() - start)

if __name__ == '__main__':
    main()