import time

# https://projecteuler.net/problem=30
# Digit fifth powers

def split_int_to_list(word):
    listofints = []
    listofstrings = [char for char in str(word)]
    for i in range(0, len(listofstrings)):
        listofints.append(int(listofstrings[i]))
    return listofints

def problem30():
	power = 5
	limit = 1000000
	result = 0
	for number in range(2, limit):
		numberList = split_int_to_list(number)
		res = sum([num**power for num in numberList])
		if res == number:
			result = result + res
	print (result)

start_time = time.time()
problem30()
print("--- %s seconds ---" % (time.time() - start_time))
