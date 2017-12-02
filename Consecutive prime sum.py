from functools import reduce

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
    primes = filterPrimes()

    summation = primes[0]
    terms = 1
    requiredPrime = 2

    while summation <= 1000000:

        for startingIndex in range(0, 5):
            summation = reduce(lambda x, y: x + y, primes[startingIndex: terms + startingIndex])

            if summation in primes and requiredPrime < summation:
                requiredPrime = summation

        terms += 1


    print(requiredPrime)

main()