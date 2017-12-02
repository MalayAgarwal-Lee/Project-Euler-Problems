'''
Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def isPalindrome(number):

    temp = number
    if list(number) == list(number)[::-1]:
        return int(temp)
    else:
        return 0


def main():

    products = set({})
    for number in range(900, 1000):

        products.update(set(map(lambda x: isPalindrome(str(number * x)), range(900, 1000))) - {0})
    print(max(products))


main()