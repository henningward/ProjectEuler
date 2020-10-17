# https://projecteuler.net/problem=25
# printe index med mer enn 1000 sifre
def problem25():
    prevFib = 1
    curFib = 1
    nextFib = 1

    for i in range(1000000):
        index = i + 3
        nextFib = prevFib + curFib
        prevFib = curFib
        curFib = nextFib

        if len(str(nextFib)) >= 1000:
            break
    print "fibonacci-tall med 1000 sifre har index", index

problem25()