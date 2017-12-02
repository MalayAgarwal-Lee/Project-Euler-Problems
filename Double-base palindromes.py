from functools import reduce

'''
Problem 36
The decimal number, 585 = 1001001001(binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''

def generatePalindromeNumbers():
    n = 1

    while n < 1000000:
        if str(n) == str(n)[::-1]:
            yield n
        n += 1

def main():
    palindromes = list(generatePalindromeNumbers())
    requiredPalindromes = []
    for item in palindromes:

        binary = bin(item)
        stringBinary = str(binary)

        if stringBinary[-1] != '0':
            reverseBinary = stringBinary[::-1]
            reverseBinary = reverseBinary[:reverseBinary.find("b0")]

            if stringBinary[2:] == reverseBinary:
                requiredPalindromes.append(item)


    print(reduce(lambda x, y: x + y, requiredPalindromes))

if __name__ == '__main__':
    main()