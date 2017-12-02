def sumDiagonalElements(n):
    if n == 5:
        return 101

    return 4*(n**2) - (6*(n - 1)) + sumDiagonalElements(n - 2)

if __name__ == '__main__':
    print(sumDiagonalElements(1001))