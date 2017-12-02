from functools import reduce

'''
Problem 50
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''

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