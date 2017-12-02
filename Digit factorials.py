from math import factorial

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

