words = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety', 100: 'onehundred', 200: 'twohundred', 300: 'threehundred', 400: 'fourhundred', 500: 'fivehundred', 600: 'sixhundred', 700: 'sevenhundred', 800: 'eighthundred', 900: 'ninehundred', 1000: 'onethousand'}

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
    letters = 3 if length == 3 else 0
    if not number in exceptions:
        for digit in number:
            if not digit == '0':
                place = 10**(length - 1)
                letters += len(words[int(digit)*place])
            length -= 1
    else:
        letters += len(words[int(number[0])*100])
        letters += len(words[int(number[1:])])

    return letters


def main():
    numbers = [i for i in range(1, 1001)]
    count = sum(map(lambda x: len(x), words.values()))
    for number in numbers:
        if number not in words.keys():
            count += getLetterCount(number)

    print(count)

if __name__ == '__main__':
    main()