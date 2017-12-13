from itertools import permutations
from functools import reduce

'''
Problem 24
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

    012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

Logic:
Not much to understand here. I simply used the permutations function to get the permutations. Since the function returns tuples containing the digits, I converted those tuples into numbers using map and reduce, and enumerated the result so that I could obtain the index of each permutation. Then, the 99999-index permutation was printed.

This is a good program to illustrate what you can do using the in-built functions of Python!
'''


def main():
    digits = map(lambda x: x, range(0, 10))
    arrangements =  permutations(digits, 10)
    numbers = enumerate(map(lambda x: reduce(lambda z, y: z*10 + y, x), arrangements))
    for key, value in numbers:
        if key == 999999:
            print(value)
            break

if __name__ == '__main__':
    main()