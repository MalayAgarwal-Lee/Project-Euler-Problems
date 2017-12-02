'''
Problem 9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

        a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

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
    print(firstNum*secondNum*thirdNum)


main()