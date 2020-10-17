import time

# https://projecteuler.net/problem=14
# Longest Collatz sequence


def nextCollatz(num):
	if (num%2 == 0):
		return num/2
	else:
		return 3*num + 1

def problem14():
	longestChain = 0
	longestChainNumber = 0
	tempNum = 0
	for number in range(1, 1000000):
		chainLength = 0
		tempNum = number
		while not number == 1:
			number = nextCollatz(number)
			chainLength = chainLength + 1
		if chainLength > longestChain:
			longestChain = chainLength
			longestChainNumber = tempNum
	print(longestChainNumber)



# Lite elegant og tregt.. ≈ 1 min
start_time = time.time()
problem14()
print("--- %s seconds ---" % (time.time() - start_time))