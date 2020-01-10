'''
Problem 7:
Find the 10001st Prime number.
'''


def sieve(limit):
    sieve = {i: False for i in range(3, limit, 2)}
    sqroot = int(limit ** (1 / 2))
    for key in range(3, sqroot, 2):
        if not sieve[key]:
            sieve.update({i: True for i in range(key * key, limit, key)})

    return [key for key, value in sieve.items() if not value]


def main():
    limit = 1500000
    reqd = 10001
    print(sieve(limit)[reqd - 2])


if __name__ == '__main__':
    main()
