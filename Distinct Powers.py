def getEvenBase():

    evenBasePowers = []

    for exponent in range(2, 101):
        evenBasePowers.append(2**exponent)

    return evenBasePowers

def getOddBase():

    oddBasePowers = []

    for exponent in range(2, 101):
        oddBasePowers.append(3**exponent)

    return oddBasePowers


def main():
    evenBase = getEvenBase()
    oddBase = getOddBase()

    for number in range(4, 101):

        for exponent in range(2, 101):

            power = number**exponent

            if number % 2 == 0:
                if power not in evenBase:
                    evenBase.append(power)
            else:
                if power not in oddBase:
                    oddBase.append(power)

    print(len(evenBase + oddBase))

if __name__ == '__main__':
    main()
