'''
Problem 21
Evaluate the sum of all the amicable numbers under 10000.
Definition of amicable numbers at https://projecteuler.net/problem=21

This problem uses the following property:
Given n, let its prime factors be p1, p2, ..., pk
Let the power of each factor be a1, a2, ..., ak
That is, n = (p1 ^ a1) X (p2 ^ a2) X ... X (pk ^ ak), where ai >= 1

Then, the sum of factors, including the number is:
sum = 1
for each prime factor pi and its corresponding power a:
    sum = sum * (the polynomial P(pi) upto a + 1 terms where all coefficients are 1)

Since all coefficients are 1, the polynomial P(pi) is GP sum with a=1, r=pi and n=a+1
Therefore, P(pi) = (pi ^ (a + 1) - 1) / (pi - 1)

This includes the number, which is subtracted to obtain the result of d(n) defined below
'''


def gp_sum(r, n):
    return (r ** n - 1) / (r - 1)


def d(n):
    number = n
    summation = 1
    count = 0

    while number % 2 == 0:
        number = number // 2
        count += 1

    summation *= gp_sum(2, count + 1)

    limit = int(number ** (1 / 2)) + 1
    for i in range(3, limit, 2):
        count = 0
        while number % i == 0:
            number = number // i
            count += 1

        if count != 0:
            summation *= gp_sum(i, count + 1)

    if number > 2:
        summation *= gp_sum(number, 2)

    return summation - n


def main():
    summation = 0
    checked = set()
    for a in range(6, 10000):
        if a not in checked:
            b = d(a)
            if b == a:
                continue
            if d(b) == a:
                summation += a + b
                checked.add(b)

    print(summation)


if __name__ == '__main__':
    main()
