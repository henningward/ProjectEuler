import time
import numpy as np
# https://projecteuler.net/problem=34
# Digit factorials

def split_int_to_list(word):
    listofints = []
    listofstrings = [char for char in str(word)]
    for i in range(0, len(listofstrings)):
        listofints.append(int(listofstrings[i]))
    return listofints


def problem34():
	limit = 1000000
	result = 0
	for number in range(3, limit):
		numberList = split_int_to_list(number)
		res = sum([np.math.factorial(num) for num in numberList])
		if res == number:
			result = result + res
	print (result)



start_time = time.time()
problem34()
print("--- %s seconds ---" % (time.time() - start_time))

