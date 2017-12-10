from functools import reduce
from time import time

'''
Problem 42
The n-th term of the sequence of triangle numbers is given by, tn = (n(n+1))/2; so the first ten triangle numbers are:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using p042_words.txt, a 16K text file containing nearly two-thousand common English words, how many are triangle words?

Solution logic:
So, this was fairly easy. There are two functions in total and a global dictionary variable. The dictionary variable contains all the letters with their corresponding position in the alphabet. 
The first function is a function to generate the triangular numbers. In the function, I figured out the upper limit for generation of the triangular numbers by obtaining the length of the largest word, which turned out to be 14. The largest possible value is the word value of the word with all the letters as Y's, which is 350 (14*25).

Now, the second function calculates the word value of a word and checks whether that word value is a triangular number or not. I instantiate the generator function in the variable, triangularNumbers. Then, I calculate the sum of the positions of the letters of the word using the map and reduce functions in conjugation. The function returns true if the sum is in the triangular number iterator, else it returns False.

Inside the context manager, I first do some string parsing to obtain all the words in a desired format. Then, I use the filter function to obtain all the words which return true when the second function is called with the words as the parameter, and take the list of the resultant list. This length is the required answer.
'''

letters = {chr(i): i - 64 for i in range(65, 91)}

def generateTriangularNumbers():
    n = 1

    triangularNumber = 1
    while triangularNumber < 350:
        triangularNumber = (n*(n + 1))/2
        yield triangularNumber
        n += 1

def getWordValue(word):
    triangularNumbers = generateTriangularNumbers()
    letterSum = reduce(lambda x, y: x + y, map(lambda x: letters[x], word))
    return True if letterSum in triangularNumbers else False


with open("p042_words.txt") as file:
    wordList = file.read().split(",")
    wordList = map(lambda x: x[x.find('"') + 1: len(x) -  1], wordList)
    triangleWords = len(list(filter(lambda x: getWordValue(x) == True, wordList)))
    print(triangleWords)


