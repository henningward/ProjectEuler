import time

# https://projecteuler.net/problem=67
# Maximum path sum II
def printPyramid(pyramid):
    for row in pyramid:
        print(row)

    print("")
    print("")

def problem67():
	f = open("problem_067.txt", "r")
	pyramid = f.read()
	pyramid = pyramid.split("\n")
	pyramid = pyramid[:-1]
	pyramid = [number.split() for number in pyramid]
	#print(pyramid[3][3])

	numberOfRows = len(pyramid)
	for row in range(numberOfRows-2, -1, -1):
		#printPyramid(pyramid)
		lengthOrRow = len(pyramid[row])
		for elem in range(lengthOrRow):
			parent1 = int(pyramid[row+1][elem])
			parent2 = int(pyramid[row+1][elem+1])
			pyramid[row][elem] = int(pyramid[row][elem]) + parent1 if parent1 > parent2 else int(pyramid[row][elem]) + parent2
    	pyramid = pyramid[:-1]

	print(pyramid[0][0])


start_time = time.time()
problem67()
print("--- %s seconds ---" % (time.time() - start_time))