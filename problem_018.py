import time

# https://projecteuler.net/problem=13
# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

def printPyramid(pyramid):
    for row in pyramid:
        print(row)

    print("")
    print("")

def problem18():

    pyramid = """
        75
        95 64
        17 47 82
        18 35 87 10
        20 04 82 47 65
        19 01 23 75 03 34
        88 02 77 73 07 63 67
        99 65 04 28 06 16 70 92
        41 41 26 56 83 40 80 70 33
        41 48 72 33 47 32 37 16 94 29
        53 71 44 65 25 43 91 52 97 51 14
        70 11 33 28 77 73 17 78 39 68 17 57
        91 71 52 38 17 14 91 43 58 50 27 29 48
        63 66 04 68 89 53 67 30 73 16 69 87 40 31
        04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
    """
    pyramid = pyramid.split("\n")
    pyramid = pyramid[1:-1]
    pyramid = [number.split() for number in pyramid]
    

    numberOrRows = len(pyramid)
    for row in range(numberOrRows-2, -1, -1):
        #printPyramid(pyramid)
        lengthOrRow = len(pyramid[row])
        for elem in range(lengthOrRow):
            parent1 = int(pyramid[row+1][elem])
            parent2 = int(pyramid[row+1][elem+1])
            pyramid[row][elem] = int(pyramid[row][elem]) + parent1 if parent1 > parent2 else int(pyramid[row][elem]) + parent2
        pyramid = pyramid[:-1]

    print(pyramid[0][0])


start_time = time.time()
problem18()
print("--- %s seconds ---" % (time.time() - start_time))
