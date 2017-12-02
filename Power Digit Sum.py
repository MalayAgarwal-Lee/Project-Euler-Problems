from functools import reduce

def main():

    result = str(2**1000)
    print(result)
    sum = reduce(lambda x, y: int(x) + int(y), result)
    print(sum)

main()