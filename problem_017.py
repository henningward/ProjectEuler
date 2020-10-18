# https://projecteuler.net/problem=17
# Number letter counts
import time

def split_int_to_list(word):
    listofints = []
    listofstrings = [char for char in str(word)]
    for i in range(0, len(listofstrings)):
        listofints.append(int(listofstrings[i]))
    return listofints



def lengthOfNumber(num):
	ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

	tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
	
	hundred = "hundred"

	thousand = "onethousand"

	numList = split_int_to_list(num)

	if (num < 20):
		return len(ones[num])

	elif (num < 100):
		return len(tens[numList[0]]) + len(ones[numList[1]]) 
	elif (num < 1000):
		if num%100 == 0:
			return len(ones[numList[0]]) + len(hundred) 
		else:
			return len(ones[numList[0]]) + len(hundred) + 3 + lengthOfNumber(int(str(num)[1:]))
	elif (num == 1000):
		return len(thousand)

def problem17():
	totalLenght = 0
	for i in range(1001):
		totalLenght = totalLenght + lengthOfNumber(i)
	print(totalLenght)

start_time = time.time()
problem17()
print("--- %s seconds ---" % (time.time() - start_time))
