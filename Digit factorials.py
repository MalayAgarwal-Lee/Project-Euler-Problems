from math import factorial

'''
Problem 34
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''

factorials = {i: factorial(i) for i in range(0, 10)}

def generateNumbers():
    n = 13

    while n <= 2540160:
        yield n
        n += 1

def getFactorialDigitSum(n):

    summation = 0
    for digit in n:
        summation += factorials[int(digit)]

    return summation

def main():

    curiousNumbers = []
    for number in generateNumbers():

        digitSum = getFactorialDigitSum(str(number))
        if digitSum == number:
            curiousNumbers.append(number)

    print(sum(curiousNumbers))


if __name__ == '__main__':
    main()

