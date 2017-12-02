'''
Problem 21
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

Solution Logic:
There are three functions: generateNumbers(), getDivisorSum() and main().
The generateNumbers() function is a generator which yields all numbers less than 10000 (upperLimit). From the problem statement and confirmation through a Wikipedia article, I found that 220 is the smallest amicable number. Therefore, I start the generation at 221.

The getDivisorSum() is a function that takes a number as an argument and returns the sum of all the proper divisors of the number. I have made a global list called divisors which has all the numbers from 1 to 9999, and the function uses this list to obtain the divisors of the number. But, the entire list is not iterated over since proper divisors of a number are less than the number itself. I obtain the index of the number and only iterate over 0 to one less than that index.

The main() function is interesting. The problem statement mentions that 220 and 284 are two amicable numbers. So, I declare a list called amicableNumbers with these two values initially. I instantiate the generator in a variable called numbers. Now, I iterate over these numbers. Due to the definition of amicable numbers, we will obtain them in paris. So, it is quite possible that a number that is to be checked is already in the list. I check for that in the first if statement inside the for loop. If the number is not in the list, I proceed by computing the sum of the divisors of the number using the getDivisorSum() function.
Here, things get interesting. There is a class of numbers called perfect numbers which are defined as numbers whose sums of proper divisors are equal to the numbers. Obviously, such numbers cannot be amicable. Thus, the check a != b. Also, it is possible that the sum of proper divisors for a number exceeds 10000. In such cases, we do not need to proceed further. Thus the check b < 10000. These two need to true together due to which an 'and' is used.
If this turns out to be the case, we proceed further by computing the sum of the proper divisors of the sum obtained previously. If this sum and the original number are equal, then the number and its sum of proper divisors are an amicable pair and are added to the list.
Lastly, I print the sum of all the numbers in the list.
'''

upperLimit = 10000
divisors = list(map(lambda x: x, range(1, upperLimit)))

def generateNumbers():
    n = 221

    while n < upperLimit:
        yield n
        n += 1

def getDivisorSum(number):

    summation = 0
    properDivisors = filter(lambda x: number % x == 0, divisors[:divisors.index(number)])
    summation = sum(properDivisors)
    return summation

def main():
    amicableNumbers = [220, 284]
    numbers = generateNumbers()

    for a in numbers:
        if a not in amicableNumbers:
            b = getDivisorSum(a)
            if a != b and b < upperLimit:
                c = getDivisorSum(b)
                if c == a:
                    amicableNumbers.extend([a, b])

    print(amicableNumbers)
    print(sum(amicableNumbers))


if __name__ == '__main__':
    main()