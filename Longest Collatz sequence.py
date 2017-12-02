from math import log2

def getCollatzSequenceLength(n):

    length = 0
    while n > 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = (3*n) + 1
        length += 1

    return length


if __name__ == '__main__':

    n = 500000
    maxLength = 0
    largestStartingNumber = 100
    numbersChecked = 0
    while n < 1000000:

        if n % 2 != 0:
            length = getCollatzSequenceLength(n)
            if length > maxLength:
                maxLength = length
                largestStartingNumber = n
            numbersChecked += 1
        n += 1
    print(largestStartingNumber, numbersChecked)
