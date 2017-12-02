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