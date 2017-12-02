from functools import reduce


'''
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.


if __name__ == '__main__':

    summation = 10405071317
    for i in range(11, 1001):
        summation += i**i

    summation = str(summation)
    length = len(summation)
    lastTenDigits = reduce(lambda x, y: x + y, summation[length - 10:])
    print(lastTenDigits)
'''



print(str(sum([i**i for i in range(11, 1001)]) + 10405071317)[-10:])
