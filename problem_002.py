# PROBLEM 2
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
def problem2():
    prevFib = 1
    curFib = 1
    nextFib = 1
    fibsum = 0
    for i in range(1000000):
        index = i + 3
        nextFib = prevFib + curFib
        prevFib = curFib
        curFib = nextFib
        if curFib%2 == 0:
            fibsum = fibsum + curFib
        if nextFib >= 4000000:
            break
    print fibsum
    print "Sum av fibonaccipartall opp til 4M: ", fibsum

problem2()