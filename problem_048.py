# https://projecteuler.net/problem=48
#last ten digit of self powers (1^1 + 2^2 + 3^3 + ... + 1000^1000
def problem48():
    powerRange = 1000
    sum = 0
    for pow in range(1, powerRange+1):
        temp = pow**pow
        sum = sum + temp % 10000000000
    sum = sum % 10000000000
    print sum

problem48()