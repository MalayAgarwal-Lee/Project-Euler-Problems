from functools import reduce

'''
Problem 20
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''


def main():

    '''
    This is a one-liner.
    I compute the factorial using the reduce() function by multiplying all numbers between 1 and 100, both inclusive. This could have also been done using the fact() function available in the math module but I used this.
    I cast the result into a string to make it iterable. I use the reduce() function on this string to add each digit of the result and print the result.
    :return:
    '''

    print(reduce(lambda x, y: int(x) + int(y), str(reduce(lambda x, y: x * y, range(1, 101)))))


main()

