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