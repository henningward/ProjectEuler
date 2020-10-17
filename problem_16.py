import time

# https://projecteuler.net/problem=16
# Power digit sum

def split_int_to_list(word):
    listofints = []
    listofstrings = [char for char in str(word)]
    for i in range(0, len(listofstrings)):
        listofints.append(int(listofstrings[i]))
    return listofints

def problem16():
	number = 2**1000
	numList = split_int_to_list(number)
	print(sum(numList))

start_time = time.time()
problem16()
print("--- %s seconds ---" % (time.time() - start_time))

