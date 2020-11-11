import time
import itertools

# https://projecteuler.net/problem=41
# Pandigital prime

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

def split_int_to_list(word):
    listofints = []
    listofstrings = [char for char in str(word)]
    for i in range(0, len(listofstrings)):
        listofints.append(int(listofstrings[i]))
    return listofints

def listToInt(n):
    return int(''.join(map(str,n)))

def problem41():
    i = 1234567
    combinations = list(itertools.permutations(split_int_to_list(i), len(str(i))))

    isPrime = False
    largestPrime = 0
    for combination in combinations:
        num = listToInt(combination)
        if IsPrime(num):
            isPrime = True
            if num > largestPrime:
                largestPrime = num
    print(largestPrime)        

start_time = time.time()
problem41()
print("--- %s seconds ---" % (time.time() - start_time))