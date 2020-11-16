##################################################################################################
##################################################################################################

                    #problemer: se https://projecteuler.net/archives

##################################################################################################
##################################################################################################


import bisect
import time
import string
import numpy as np
    
#primes = [prime for prime in range(upr) if IsPrime(prime)] 
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

def listToInt(n): return int(''.join(map(str,n)))


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


def isUniqueChars(st): 
  
    # String length cannot be more than 
    # 256. 
    if len(st) > 256: 
        return False
  
    # Initialize occurrences of all characters 
    char_set = [False] * 128
  
    # For every character, check if it exists 
    # in char_set 
    for i in range(0, len(st)): 
  
        # Find ASCII value and check if it 
        # exists in set. 
        val = ord(st[i]) 
        if char_set[val]: 
            return False
  
        char_set[val] = True
  
    return True


start_time = time.time()
#problemX()
print("--- %s seconds ---" % (time.time() - start_time))



""" template

import time

# https://projecteuler.net/problem=45
# Triangular, pentagonal, and hexagonal

def Main():

    return (":(")



start_time = time.time()
result = Main()

print("--- %s seconds ---" % (time.time() - start_time))
print("----------------------------------")
print("result: " + str(result))
print("----------------------------------")



"""