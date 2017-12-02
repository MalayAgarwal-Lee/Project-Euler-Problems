def main():

    firstNum = secondNum = 0
    c = 0
    for a in range(100, 500):

        for b in range(a +  1, 500):
            if ((1000*(a+b)) - 500000 - (a*b)) == 0:
                firstNum = a
                secondNum = b
                c =  1
                break
        if c == 1:
            break

    thirdNum =  ((firstNum**2 + secondNum**2)**(1/2))
    print(firstNum, secondNum, thirdNum)
    print(firstNum*secondNum*thirdNum)


main()