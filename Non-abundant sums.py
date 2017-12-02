from math import floor
import time

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