import time

# https://projecteuler.net/problem=28
# Number spiral diagonals

def an(n):
	return 4 * n**2 + 4 * n + 1

def bn(n):
	return 4 * n**2 - 2 * n + 1

def cn(n):
	return 4 * n**2 + 1

def dn(n):
	return 4 * n**2 + 2 * n + 1


def problem28():
	
	diagSum = 1
	for i in range(1, 501):
		diagSum = diagSum + an(i) + bn(i) + cn(i) + dn(i)
	print(diagSum)
start_time = time.time()
problem28()
print("--- %s seconds ---" % (time.time() - start_time))

#25
#101