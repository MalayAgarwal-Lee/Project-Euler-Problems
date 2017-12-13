from math import sqrt

'''
Problem 46
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×(1^2)
15 = 7 + 2×(2^2)
21 = 3 + 2×(3^2)
25 = 7 + 2×(3^2)
27 = 19 + 2×(2^2)
33 = 31 + 2×(1^2)

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

Solution logic:
Here, we need to do two main things. Firstly, we need to generate all the primes up to a certain limit. Secondly, we need check all odd composite numbers up to that limit, and stop when there is a number within that range which does not satisfy the above property. 

For the first task, I make use of the Sieve of Eratosthenes. Intuitively, in this, we take a grid of numbers starting from 2 up to some limit. Taking each number, we cross out all the multiples of that number in the grid. Say we take 2. We will then cross out 4, 6, 8 and so on. When we have exhausted all numbers, the uncrossed numbers will be prime. 
To implement this in Python, I make use of a dictionary where I take all the numbers from 2 to a certain limit as the keys and set their values as False. Here, False represents an uncrossed number. Now, we can optimize this. Since 2 is the only even prime, the dictionary does not need to contain any other even numbers. Moreover, since there are no even numbers other than 2 in the dictionary, we can easily start from 3. 
Also, when we start with a number, its multiples will be crossed out. Then, when we will start with the next number, it is easy to see that all its multiples below its square will be crossed out due to the previous numbers, and we do not need to start crossing out multiples below the square. Also, since our dictionary does not have any even numbers except 2, we do not need to check for even multiples of a number, and need to check only the odd multiples.

Now, that's out of the way. 
Moving ahead, the next function is quite simple. It makes a map object of squares less than the number. It goes over each one of them, subtracting them from the number. If the result is prime, it returns True and if not, it returns False. 

That's about it. The main function simply prints the first number which returns False.
'''

limit = 10000

def getPrimes():
    upperLimit = limit + 1
    sieve =  {2: False}
    sieve.update({i: False for i in range(3, upperLimit, 2)})

    for key in list(sieve.keys())[1:]:

        if not sieve[key]:
            for i in range(key**2, upperLimit, 2):
                if i % key == 0:
                    sieve[i] = True

    return list(filter(lambda x: sieve[x] == False, sieve.keys()))

def checkSum(number, primes):
    squares = map(lambda x: x ** 2, range(1, int(sqrt(number))))
    for square in squares:
        if (number - 2*square) in primes:
            return True
    return False


def main():
    primes = getPrimes()
    numbers = filter(lambda x: x not in primes, range(9, limit, 2))
    for number in numbers:
        if not checkSum(number, primes):
            print(number)
            break


if __name__ == '__main__':
    main()