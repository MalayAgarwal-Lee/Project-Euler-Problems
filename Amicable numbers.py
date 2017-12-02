upperLimit = 10000
divisors = list(map(lambda x: x, range(1, upperLimit)))

def generateNumbers():
    n = 221

    while n < upperLimit:
        yield n
        n += 1

def getDivisorSum(number):

    summation = 0
    properDivisors = filter(lambda x: number % x == 0, divisors[:divisors.index(number)])
    summation = sum(properDivisors)
    return summation

def main():
    amicableNumbers = [220, 284]
    numbers = generateNumbers()

    for a in numbers:
        if a not in amicableNumbers:
            b = getDivisorSum(a)
            if a != b and b < upperLimit:
                c = getDivisorSum(b)
                if c == a:
                    amicableNumbers.extend([a, b])

    print(amicableNumbers)
    print(sum(amicableNumbers))


if __name__ == '__main__':
    main()