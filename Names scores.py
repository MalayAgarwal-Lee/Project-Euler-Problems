from functools import reduce

'''
Problem 22
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''

alphabetScore = {chr(x): x-64 for x in range(65, 91)}

with open("p022_names.txt") as file:
    nameList = str(file.read()).split(',')
    nameList = list((map(lambda x: x[x.find("") + 1: len(x) - 1], nameList)))
    nameList.sort()
    positionalList = dict(enumerate(nameList))
    summation = 0
    for position, name in positionalList.items():
        summation += (position + 1) * reduce(lambda x, y: x + y, map(lambda x: alphabetScore[x], name))

    print(summation)
