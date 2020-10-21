import time

# https://projecteuler.net/problem=29
# Distinct powers

def problem29():
	result = []
	upperLim = 101
	for a in range(2, upperLim):
		for b in range(2, upperLim):
			if (a**b not in result):
				result.append(a**b)
	result = sorted(result)
	print(len(result))
start_time = time.time()
problem29()
print("--- %s seconds ---" % (time.time() - start_time))
