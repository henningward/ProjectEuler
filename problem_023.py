import time
import numpy as np
# https://projecteuler.net/problem=23
# Non-abundant sums

def IsAbundant(num):
	divisorSum = 0

	for i in range(1, int(num/2) + 1):
		if i is not num:
			if num%i == 0:
				divisorSum = divisorSum + i
				if divisorSum > num:
					return True
	return False

def binarySearch(arr, l, r, x):
    # Check base case
    if r >= l:

        mid = (l + (r - l) //2)

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

            # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)

            # Else the element can only be present in right subarray
        else:
            return binarySearch(arr, mid + 1, r, x)

    else:
        # Element is not present in the array
        return -1




def problem23():
	abundantNumbers = []
	#for i in range(1, 28124):
	limit = 28124

	lower_lim = 1
	#limit = 300
	for i in range(lower_lim, limit):
		if IsAbundant(i):
			abundantNumbers.append(i)
	sumOfAbundant = []
	pctComplete = -1
	abundantNumbers = sorted(abundantNumbers)
	for i in range(0, len(abundantNumbers)):
		if pctComplete is not int((1000*i/len(abundantNumbers))):
			pctComplete = int((1000*i/len(abundantNumbers)))
			print("Percent complete: " + str(float(pctComplete)/10))
		for j in range(i, len(abundantNumbers)):
			AbSum = abundantNumbers[i] + abundantNumbers[j]
			if AbSum < limit:
				if (binarySearch(sumOfAbundant, 0, len(sumOfAbundant)-1, AbSum) == -1):
					#if (binarySearch(abundantNumbers, 0, len(abundantNumbers)-1, AbSum) is not -1):
					sumOfAbundant.append(AbSum)
					sumOfAbundant = sorted(sumOfAbundant)

	
	sum_sum = 0	
	for i in range(1, sumOfAbundant[-1] + 1): 
	    sum_sum = sum_sum + i
	
	print(sum_sum- sum(sumOfAbundant))
	#print((sumOfAbundant))
	#print(sum_sum)
start_time = time.time()
problem23()
print("--- %s seconds ---" % (time.time() - start_time))

