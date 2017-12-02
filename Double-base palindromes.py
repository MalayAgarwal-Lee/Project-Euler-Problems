from functools import reduce

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