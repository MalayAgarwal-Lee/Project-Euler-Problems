'''
Problem 39
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
'''


pValues = map(lambda x: x, range(121, 1000))

def getNumberOfSolutions(p):
    solutionCount = 0
    pSquare = p**2
    l = []
    for a in range(1, p - 1):
        b = int(((2*p*a) - pSquare)/(2*(a - p)))

        if b != 0:
            c = (a**2 + b**2)**(1/2)

            if a + b + c == p and c <= (a + b):
                triangle = [a, b, c]
                triangle.sort()
                if triangle not in l:
                    solutionCount += 1
                    l.append(triangle)

    return solutionCount


def main():
    maxSolutions = 3
    requiredValue = 0
    for p in pValues:
        solutionCount = getNumberOfSolutions(p)
        if solutionCount > maxSolutions:
            maxSolutions = solutionCount
            requiredValue = p

    print(requiredValue, maxSolutions)


if __name__ == '__main__':
    main()
