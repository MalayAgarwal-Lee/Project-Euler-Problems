def generateInfiniteRange():

    a = 2520

    while True:
        yield a
        a += 20


def checkDivisibility(number):


    for i in range(11, 20):
        if not number % i == 0:
            return False
    return True


def main():

    infiniteRange = generateInfiniteRange()
    while True:

        number = next(infiniteRange)
        if checkDivisibility(number):
            print(number)
            break


if __name__ == '__main__':
    main()