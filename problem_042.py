import time
import itertools

# https://projecteuler.net/problem=42
# Coded triangle numbers

def CalculateNameValue(name):
	result = 0
	for letter in name:

		result = result + ord(letter.lower()) - 96
	return result

def binarySearch(arr, l, r, x):
    # Check base case
    if r >= l:

        mid = int(l + (r - l) / 2)

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

def problem42():
    result = 0

    f = open("p042_words.txt", "r")
    names = f.read()
    names = [name[1:-1] for name in sorted(names.split(","))]

    triangleNumbers = []
    for n in range(1, 100):
        triangleNumbers.append(int(0.5 * n * (n + 1)))
    for name in names:
        val = CalculateNameValue(name)
        if not binarySearch(triangleNumbers, 0, len(triangleNumbers)-1, int(val)) == -1:
            result = result + 1
    print(result)

start_time = time.time()
problem42()
print("--- %s seconds ---" % (time.time() - start_time))