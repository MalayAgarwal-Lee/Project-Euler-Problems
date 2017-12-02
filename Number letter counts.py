'''
Problem 17
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''

words = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety', 100: 'onehundred', 200: 'twohundred', 300: 'threehundred', 400: 'fourhundred', 500: 'fivehundred', 600: 'sixhundred', 700: 'sevenhundred', 800: 'eighthundred', 900: 'ninehundred', 1000: 'onethousand'}


#the program's logic relies on the fact that each digit of a number contributes to its name
#for example, 132 is one hundred and thirty two. Here the one hundred comes from the first digit (1), the thirty comes from the second digit (3) and the two comes from the third digit (2). This logic works fine for all numbers except those of the type x1y where 1 <= x, y <= 9 (example - 111, 112, 113, 211, 919, etc.). This is because all numbers up to twenty have a unique naming scheme. After twenty, the names are obtained by using the names of smaller numbers. 20 is twenty while 21 is twenty-one, which is obtained by joining the names for the numbers 20 and 1.
#therefore, I made an exceptions list which contains all the numbers of x1y type.
#I handle them separately when calculating the letter count
exceptions = []
exceptions.extend([str(i) for i in range(111, 120)])
exceptions.extend([str(i) for i in range(211, 220)])
exceptions.extend([str(i) for i in range(311, 320)])
exceptions.extend([str(i) for i in range(411, 420)])
exceptions.extend([str(i) for i in range(511, 520)])
exceptions.extend([str(i) for i in range(611, 620)])
exceptions.extend([str(i) for i in range(711, 720)])
exceptions.extend([str(i) for i in range(811, 820)])
exceptions.extend([str(i) for i in range(911, 920)])


def getLetterCount(number):
    number = str(number)
    length = len(number)

    #all numbers which have three digits will make use of an 'and', which has three characters
    letters = 3 if length == 3 else 0
    if not number in exceptions:
        for digit in number:
            if not digit == '0':
                #place indicates the place the digit occupies (ones, tens, hundreds)
                place = 10**(length - 1)

                #here, the length of each component of the name of the number is added to the variable letters
                #int(digit)*place is used to obtain the value of the digit in the number
                #example: In 132, for the first iteration, the digit is 1. Its place is 100. int(digit)*place will be 1*100 = 100. The value corresponding to this key is retrieved from the dictionary, its length computed and added.
                #In the second iteration, the digit will be 3, its place 10. int(digit)*place computes to 3*10 = 30. So on and so forth.
                letters += len(words[int(digit)*place])
            length -= 1

    #handling numbers in the exceptions list
    else:
        #these numbers will be greater than 100
        #so, I take the first digit, multiply it by hundred and retrieve its corresponding value from the dict
        letters += len(words[int(number[0])*100])

        #the next two digits will be anything from 11 to 19. So, I simply take the number obtained from these two digits as the key and retrieve the corresponding value from the dict
        letters += len(words[int(number[1:])])

    return letters


def main():
    numbers = [i for i in range(1, 1001)]
    #I am setting count as the sum of the names of all the numbers already in the dict
    count = sum(map(lambda x: len(x), words.values()))
    for number in numbers:
        #as the sum of name of all the numbers in the dict has already been considered, I am only calculating the sum for numbers not in the dict
        if number not in words.keys():
            count += getLetterCount(number)

    print(count)

if __name__ == '__main__':
    main()