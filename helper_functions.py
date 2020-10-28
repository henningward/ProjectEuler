##################################################################################################
##################################################################################################

                    #problemer: se https://projecteuler.net/archives

##################################################################################################
##################################################################################################


import bisect
import time
import string
import numpy as np
    
def IsPrime(number):

    newPrime = True
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True

def IsPrime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True

def IsPrimeOLD(primes, number):

    newPrime = True
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True

    for prime in primes:
        if number%prime == 0:
            newPrime = False
    return newPrime

def split_int_to_list(word):
    listofints = []
    listofstrings = [char for char in str(word)]
    for i in range(0, len(listofstrings)):
        listofints.append(int(listofstrings[i]))
    return listofints


def binarySearch(arr, l, r, x):
    # Check base case
    if r >= l:

        mid = l + (r - l) / 2

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





start_time = time.time()
#problemX()
print("--- %s seconds ---" % (time.time() - start_time))

