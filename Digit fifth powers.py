'''
Problem 30
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''

powers = {i: i**5 for i in range(0, 10)}

def generateNumbers():
    n = 10

    while n <= 236196:
        yield n
        n += 1

def getPowerDigitSum(n):
    summation = 0
    for digit in n:
        summation += powers[int(digit)]

    return summation

def main():

    fifthPowers = []
    for number in generateNumbers():
        digitSum = getPowerDigitSum(str(number))
        if digitSum == number:
            fifthPowers.append(number)

    print(sum(fifthPowers))

if __name__ == '__main__':
    main()