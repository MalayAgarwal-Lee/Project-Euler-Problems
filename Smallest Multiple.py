'''
Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

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