def generateFibonacci():
    a = 64128128989018176585252040302126085488071926335079419810451272680747571571160723032344138301571590200724086190900349998530438936403887378198185
    b = 103761492339168842018587530858475070677646106130118753779820168511287979391742270610548339362599898075442971926458625775220986965441725618892473
    while True:
        yield a
        a, b = a, a + b

if __name__ == '__main__':

    fibonacciSequence = generateFibonacci()
    i = 1
    while True:

        currentTerm = str(next(fibonacciSequence))
        if len(currentTerm) == 1000:
            print(currentTerm)
            print(i)
            break
        i += 1