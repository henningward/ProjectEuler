import time
import itertools

# https://projecteuler.net/problem=51
# Prime digit replacements

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

def listToInt(n): return int(''.join(map(str,n)))

#Prime number n with repeating digit at index "indicies". Check how many resulting numbers that becomes primes. Returns this number
def FamilyNumber(n, indices, mf):
    n = split_int_to_list(n)
    nOriginal = n[:]

    #Create all valid combinations of digit indices to be replaced
    iPermutations = []
    for i in range(2, len(indices)):
        iPermutations = iPermutations + (list(itertools.combinations(indices, i)))

    maxFamily = mf
    
    result = [0, 0]
    for permutation in iPermutations:
        minimumNumber = 0
        family = 0
        n = nOriginal[:]
        for i in range(9, -1, -1):
            for index in permutation:
                n[index] = i
            if IsPrime(listToInt(n)) and len(str(listToInt(n))) == len(str(listToInt(nOriginal))):
                minimumNumber = listToInt(n)
                family = family + 1
        if family > maxFamily:
            maxFamily = family
            result = [maxFamily, minimumNumber]
    return result
        
def problem51():
    upr = 1000000
    primes = [prime for prime in range(upr) if IsPrime(prime)] 
    maxFamily = 0
    minimumNumber = 0
    for prime in primes:
        llist = split_int_to_list(prime)

        for n in range(10):
            indicies = ([i for i,x in enumerate(llist) if x==n])
            if len(indicies) > 1:
                result = FamilyNumber(listToInt(llist), indicies, maxFamily)
                family = result[0]

                if family > maxFamily:
                    maxFamily = family
                    minimumNumber = result[1]

    return ("family number: " + str(maxFamily) + " gives minimum number: " + str(minimumNumber))

start_time = time.time()
result = problem51()

print("--- %s seconds ---" % (time.time() - start_time))
print("----------------------------------")
print("result: " + str(result))
print("----------------------------------")
