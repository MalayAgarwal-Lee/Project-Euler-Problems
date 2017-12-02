from functools import reduce

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
