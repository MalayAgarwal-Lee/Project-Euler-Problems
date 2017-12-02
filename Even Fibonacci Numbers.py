from functools import reduce

#every third term in the Fibonacci sequence is even
#the code below only calculates these terms
#hence, there is no need to check whether a particular fibonacci number is even or not
def generateFibonacci():
    a = 1
    b = 1
    c = a + b
    while a < 40000000:
        yield c
        a = c + b
        b = a + c
        c = a + b


def main():
    summation = reduce(lambda x, y: x + y, generateFibonacci())
    print(summation)


if __name__ == '__main__':
    main()


