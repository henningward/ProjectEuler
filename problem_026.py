import time
import decimal

# https://projecteuler.net/problem=26
# Reciprocal cycles

def split_int_to_list(word):
    listofints = []
    listofstrings = [char for char in str(word)]
    for i in range(0, len(listofstrings)):
        listofints.append(int(listofstrings[i]))
    return listofints


def IsReciprocal(fraction):
	strfraction = str(fraction)

	for i in range(1, int(len(strfraction)/2)):
		recurringFraction = strfraction[0:i]
		remainingFraction = strfraction[i:i+i]
		if recurringFraction == remainingFraction:
			return i
	return -1


def problem26():
	decimalLength = 10000
	decimal.setcontext(decimal.Context(prec=decimalLength))
	limit = 1001
	longestRecurring = 0
	longestIndex = 0
	for i in range(1, limit+1):
		fraction = int(decimal.Decimal(1.0) / decimal.Decimal(i) * 10**decimalLength)
		
		if (IsReciprocal(fraction) > longestRecurring):
			longestRecurring = IsReciprocal(fraction)
			print(longestRecurring)
			longestIndex = i
	print(longestIndex)

		#if subList in fractionList[longestRecurring:]:




start_time = time.time()
problem26()
print("--- %s seconds ---" % (time.time() - start_time))

