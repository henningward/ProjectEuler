# https://projecteuler.net/problem=6
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
def problem6():
    squareofsum = 0
    sumofsquares = 0
    naturalsum = 0
    for i in range(101):
        sumofsquares = sumofsquares + i**2
        naturalsum = naturalsum + i
    squareofsum = naturalsum**2
    result = squareofsum - sumofsquares
    print "differansen mellom square of sum og sum of squares er ", result


problem6()