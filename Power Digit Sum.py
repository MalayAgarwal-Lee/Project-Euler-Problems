from functools import reduce

'''
Problem 16
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
'''

def main():

    result = str(2**1000)
    print(result)
    sum = reduce(lambda x, y: int(x) + int(y), result)
    print(sum)

main()