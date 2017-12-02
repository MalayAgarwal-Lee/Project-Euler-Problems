'''
Problem 28
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

        21 22 23 24 25
        20  7  8  9 10
        19  6  1  2 11
        18  5  4  3 12
        17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

Solution logic:
If we look at a 5 by 5 spiral, we'll see that the sum of all the diagonal elements is the sum of all the corner elements of the spiral and the sum of all the diagonal elements of a 3 by 3 spiral.

Example:
21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

If D(n) represents the sum of the diagonal elements of a n by n spiral, then
D(5) = 25 + 21 + 17 + 13 + D(3)

We can write 21 = 25 - (5 - 1), 17 = 25 - 2*(5 - 1) and 13 = 25 - 3*(5 - 1)
Thus, D(5) can be written as:
D(5) = 25 + (25 - (5 - 1)) + (25 - 2*(5 - 1)) + (25 - 3*(5 - 1)) + D(3)
Now, if we replace 5 by n, 25 by n^2 and 3 by n - 2, we get:

D(n) = n^2 + (n^2 - (n - 1)) + (n^2 - 2*(n - 1)) + (n^2 - 3*(n - 1)) + D(n - 2)

Opening all the brackets and grouping similar terms, the above expression simplifies to:
D(n) = 4*(n^2) - 6*(n - 1) + D(n - 2)

This provides a good base to apply a recursive technique for computing the sum.
'''

def sumDiagonalElements(n):
    if n == 5:
        return 101

    return 4*(n**2) - (6*(n - 1)) + sumDiagonalElements(n - 2)

if __name__ == '__main__':
    print(sumDiagonalElements(1001))