import time
import itertools
# https://projecteuler.net/problem=35
# Circular primes


def IsPrime(n):
	if n == 2 or n == 3: return True
	if (n < 2) or (n%2 == 0): return False
	if n < 9: return True
	if n%3 == 0: return False
	r = int(n**0.5)
	f = 5
	while f <= r:
		if n%f == 0: return False
		if n%(f+2) == 0: return False
		f +=6
	return True

def split_int_to_list(word):
    listofints = []
    listofstrings = [char for char in str(word)]
    for i in range(0, len(listofstrings)):
        listofints.append(int(listofstrings[i]))
    return listofints

def Rotations(value):

	lengthOfInt = len(str(value))
	results = []
	strvalue = str(value)
	for shift in range(lengthOfInt):
		res = (strvalue * 3)[len(strvalue) + shift :  
					2 * len(strvalue) + shift] 
		results.append((res))

	return results

def problem35():
	result = 1 #Because 2 is a solution
	for i in range(2, 1000000):
		if (i%20000 == 0):
			pct = i / 1000000 * 100
			print(str(pct) + " percent done")

		if not IsPrime(i):
			continue
		if "2" in str(i) or "4" in str(i) or "6" in str(i) or "8" in str(i) or "0" in str(i):
			continue

		#combinations = list(itertools.permutations(split_int_to_list(i), len(str(i))))
		combinations = Rotations(i)
		circularPrime = True
		for combination in combinations:
			temp = ""
			for i in range(len((combination))):
				temp = temp + str((combination[i]))
			combination = int(temp)
			if not IsPrime(combination):
				circularPrime = False
				break
		if (circularPrime):
			#print(combination)
			result = result + 1

	print(result)


start_time = time.time()
problem35()
print("--- %s seconds ---" % (time.time() - start_time))