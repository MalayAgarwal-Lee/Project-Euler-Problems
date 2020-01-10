def sieve(limit):
    sieve = {i: False for i in range(3, limit, 2)}
    sqroot = limit ** (1/2)
    n = 0
    key, value = sieve.items()[n]
    while key <= sqroot:
        if not value:
            sieve.update({i: True for i in range(key * key, limit, key)})

        n += 1
        key, value = sieve.items()[n]

    return [key for key, value in sieve.items() if not value]


def main():
    limit = 100000
    print(sieve(limit))


if __name__ == '__main__':
    main()