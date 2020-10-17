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


def is_prime(n):
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

# https://projecteuler.net/problem=60
# Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime
#
# .

def Get_primes_from_Sieve(n):
    # Create a boolean array "prime[0..n]" and initialize
    #  all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):

        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):

            # Update all multiples of p
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    # Add primes to list
    primes = []
    for p in range(2, n):
        if prime[p]:
            primes.append(p)
    return primes


def problem60():
    def IsPrimePair(primes, prime1, prime2):
        primecombo1 = int(str(prime1) + str(prime2))
        primecombo2 = int(str(prime2) + str(prime1))
        res1 = binarySearch(primes, 0, len(primes)-1, primecombo1)
        res2 = binarySearch(primes, 0, len(primes)-1, primecombo2)
        if (res1 is not -1) and (res2 is not -1):
            return True
        else:
            return False

    def IsPrimesConcatenateOLD(all_primes, primes):
        #print primes
        for i in range(len(primes)):
            for j in range(len(primes)):
                if i != j:
                    primecombo = int(str(primes[i]) + str(primes[j]))
                    if binarySearch(all_primes, 0, len(all_primes) - 1, primecombo) is -1:
                        return False

        return True

    def IsPrimesConcatenate(all_primes, primes, new_prime):
        for prime in primes:
            primecombo1 = int(str(prime) + str(new_prime))
            primecombo2 = int(str(new_prime) + str(prime))

            #search1 = binarySearch(all_primes, 0, len(all_primes) - 1, primecombo1)
            #search2 = binarySearch(all_primes, 0, len(all_primes) - 1, primecombo2)
            if (not is_prime(primecombo1) )or (not is_prime(primecombo2)):
                return False
        return True

    primes = Get_primes_from_Sieve(1000000)
    primes.sort()

    def addConcatenates(ALLPRIMES, prime_list, upper_limit):
        temp_list = []
        ctr = float(0)
        tmppercnt = 0
        for primes in prime_list:

            ctr = ctr + 1
            prcnt = ctr / float(len(prime_list))
            prcnt = int(prcnt * 100)

            if prcnt%10 == 0 and tmppercnt != prcnt:
                tmppercnt = prcnt
                print prcnt, "% fullfort"

            #primes.sort()
            if isinstance(primes, int):
                primes = [primes]


            lower_limit = binarySearch(ALLPRIMES, 0, len(ALLPRIMES), max(primes))
            for i in range(lower_limit, upper_limit):
                prime_eval = ALLPRIMES[i]
                if IsPrimesConcatenate(ALLPRIMES, primes, prime_eval):
                    temp_list.append(primes + [prime_eval])
        return temp_list



    primeConcatenates = [3, 7, 11, 13, 17]
    #print primeConcatenates
    print "run 1/4:"
    primeConcatenates = addConcatenates(primes, primeConcatenates, 6000)
    print "grupper med to primes: \n", primeConcatenates
    print "run 2/4:"
    primeConcatenates = addConcatenates(primes, primeConcatenates, 7000)
    print "grupper med tre primes: \n", primeConcatenates
    print "run 3/4:"
    primeConcatenates = addConcatenates(primes, primeConcatenates, 8000)
    print "grupper med fire primes: \n", primeConcatenates
    print "run 4/4:"
    primeConcatenates = addConcatenates(primes, primeConcatenates, 10000)
    print "grupper med fem primes: \n", primeConcatenates

    best_sum = 10000000
    best_primes = []
    for primes in primeConcatenates:
        current_sum = sum(primes)
        if current_sum < best_sum:
            best_sum = current_sum
            best_primes = primes

    print "beste kombinasjonen av primes:"
    print best_primes
    print "som gir summen:", best_sum

problem60()