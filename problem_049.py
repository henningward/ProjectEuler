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

def ConfirmValidResult(llist):
    for i in range(len(llist)):
        for j in range(i+1, len(llist)):
            d = abs(llist[i] - llist[j])
            for k in range(j+1, len(llist)):
                if abs(llist[j] - llist[k]) == d:
                    return [llist[i],llist[j],llist[k] ]
    return False
        

def problem49():
    combinations = list(itertools.product(split_int_to_list(1234567890), repeat = 4))
    
    
    combinations = [listToInt(combination) for combination in combinations]
    cprimes = []

    for combination in combinations:
        if IsPrime((combination)):
            cprimes.append(combination)
    combinations = cprimes


        #elif len(str(combinations[i])) == 3:
        #    combinations.pop(i)
    #print(combinations)
    for c in combinations:
        if not IsPrime(c):
            print(":O")
    #combinations = sorted(combinations)
    #combinationsSorted = [listToInt(sorted(str(c))) for c in combinations]
    #print(combinations)

    inc = []
    itr = 0


    for i in range(len(combinations)):
        permutations = []
        c1 = combinations[i]
        inc = []

        if len(str(c1)) == 4:
            permutations.append(c1)
            for j in range(i+1, len(combinations)):
                c2 = combinations[j]
                if IsPermutation(c1, c2) and len(str(c2)) == 4:
                    permutations.append(c2)
                    for permutation in permutations:
                        d = abs(permutation - c2)
                        #if d == 3330:
                        #    print(c2)
                        if not d == 0 and len(str(d)) == 4:
                            if d in inc:
                               
                                if (ConfirmValidResult(permutations)):
                                    result =  (ConfirmValidResult(permutations))
                                    result = sorted(result)
                                    st = ""
                                    for r in result:
                                        st = st + str(r)
                                    if not int(st) == 148748178147:
                                        return int(st)
                                   

                            else:
                                inc.append(d)
                    
                        
                    

        
        

    return ":("


start_time = time.time()
result = problem49()

print("--- %s seconds ---" % (time.time() - start_time))
print("----------------------------------")
print("result: " + str(result))
print("----------------------------------")
