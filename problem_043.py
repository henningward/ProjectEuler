import time
import itertools

# https://projecteuler.net/problem=43
# Sub-string divisibility

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


def NewPermutations(notToBeIncluded = "", length):
    substr = ""
    for i in range(10):
        if str(i) not in str(notToBeIncluded):
            substr = substr + str(i)

    temp = list(itertools.permutations(split_int_to_list(substr), length))
    triplePermutations = []
    for combination in temp:
        triplePermutations.append(listToInt(combination))

    return triplePermutations

def NextPermutation(sub, n):

    result = 0
    permutations = NewPermutations(sub)
    for permutation in permutations:
        if (n == 2):
            print(n)
        if permutation%n == 0:
            if n == 9:
                return True
            result = result + NextPermutation(permutation, n + 1)
    return False
def problem43():

    #divisors = [2, 3, 5, 7, 11, 13, 17]
    
    #d6 = 5

    for i in range(10000):
        if i%11 == 0:
            print(i)

    #n = 1234567890
    #temp = list(itertools.permutations(split_int_to_list(n)))
    #Permutations = []
    #for combination in temp:
    #    Permutations.append(listToInt(combination))
    #print(NextPermutation("", 2))
    
  



    #print(triplePermutations)

start_time = time.time()
problem43()
print("--- %s seconds ---" % (time.time() - start_time))