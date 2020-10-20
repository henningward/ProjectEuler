import time
import numpy as np
# https://projecteuler.net/problem=20
# Factorial digit sum
def split_int_to_list(word):
    listofints = []
    listofstrings = [char for char in str(word)]
    for i in range(0, len(listofstrings)):
        listofints.append(int(listofstrings[i]))
    return listofints


def problem20():

	fact = 1
	for i in range(1,101): 
		fact = fact * i 
	strfact = split_int_to_list(fact)
	print(sum(strfact))

start_time = time.time()
problem20()
print("--- %s seconds ---" % (time.time() - start_time))

