import time
import itertools
# https://projecteuler.net/problem=45
# Triangular, pentagonal, and hexagonal

def split_int_to_list(word): return [int(char) for char in str(word)]

def listToInt(n):
    return int(''.join(map(str,n)))

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

def IsPermutation(a, b): return sorted(str(a)) == sorted(str(b))

def problem49():
    combinations = list(itertools.permutations(split_int_to_list(1234567890), 4))
    combinations = [listToInt(combination) for combination in combinations]

    for i in range(len(combinations) -1, -1, -1):
        if not IsPrime(combinations[i]):
            combinations.pop(i)
        #elif len(str(combinations[i])) == 3:
        #    combinations.pop(i)

    #combinations = sorted(combinations)
    #combinationsSorted = [listToInt(sorted(str(c))) for c in combinations]
    #print(combinations)
    
    inc = []
    itr = 0

    for i in range(len(combinations)):
        permutations = []
        c1 = combinations[i]
        permutations.append(c1)
        inc = []
        itr = 0
        for j in range(i, len(combinations)):
            c2 = combinations[j]
            if IsPermutation(c1, c2):
                permutations.append(c2)
                for permutation in permutations:
                    d = abs(permutation - c2)
                    if not d == 0:
                        if d in inc:
                            itr = itr + 1
                            if itr == 1:
                                return d
                        else:
                            inc.append(d)
  
            



    return ":("

"""
    combinations = [x for _,x in sorted(zip(combinations,combinationsSorted))]
    combinationsSorted = sorted(combinationsSorted)

    #print(combinations)
    #print("----")
    #print(combinationsSorted)
    success = False
    index = 0

    while not success:
        
        currentPermutation = combinationsSorted[index]
        inc = []
        itr = 0
        for i in range(index, len(combinations)):
            if combinationsSorted[i] is not currentPermutation:
                if index < len(combinations) - 2:
                    index = i + 1
                else:
                    return 0
                #print(index)
                break
            combination = combinations[i]

            if combination in inc:
                itr = itr + 1
            inc.append(combination)
            print(inc)

            if itr == 3:
                return combination
            
"""






start_time = time.time()
result = problem49()

print("--- %s seconds ---" % (time.time() - start_time))
print("----------------------------------")
print("result: " + str(result))
print("----------------------------------")
