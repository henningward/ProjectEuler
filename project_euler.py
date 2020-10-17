##################################################################################################
##################################################################################################

                    #problemer: se https://projecteuler.net/archives

##################################################################################################
##################################################################################################


import bisect
import time
import string
import numpy as np
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

def IsPrime(primes, number):

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

# PROBLEM 1
# Find the sum of all the multiples of 3 or 5 below 1000
def problem1():
    sum = 0
    for i in range(1, 1000):
        if i%3==0 or i%5==0:
            sum = sum + i
    print(sum)

# PROBLEM 2
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
def problem2():
    prevFib = 1
    curFib = 1
    nextFib = 1
    fibsum = 0
    for i in range(1000000):
        index = i + 3
        nextFib = prevFib + curFib
        prevFib = curFib
        curFib = nextFib
        if curFib%2 == 0:
            fibsum = fibsum + curFib
        if nextFib >= 4000000:
            break
    print fibsum
    print "Sum av fibonaccipartall opp til 4M: ", fibsum

# PROBLEM 3
# What is the largest prime factor of the number 600851475143 ?
def problem3():

    primes = [2, 3, 5]
    i = 3
    thePrime = 600851475143
    def searchForPrimeFactors(limit):
        for i in range(limit):
            i = i+1
            if IsPrime(primes, i):
                primes.append(i)
        thePrime = 600851475143
        largestPrime = 0
        for prime in primes[::-1]:
            if thePrime % prime == 0:
                if largestPrime == 0:
                    largestPrime = prime
                thePrime =  thePrime / prime
        return thePrime, largestPrime

    factr = 1
    while thePrime > 1:
        factr = factr * 5
        thePrime, largestPrime = searchForPrimeFactors(factr)
        if thePrime == 1:
            print "largest prime factor:", largestPrime

# PROBLEM 4
# Find the largest palindrome made from the product of two 3-digit numbers.
def problem4():
    products = []
    for i in range(100, 1000):
        for j in range(100, 1000):
            products.append(i*j)
    products.sort()
    for integ in products[::-1]:
        tempInt = split_int_to_list(integ)
        tempIntRev = tempInt[::-1]
        if tempInt == tempIntRev:
            print "storste palindrome-produkt er", ''.join(map(str, tempIntRev))
            break

# PROBLEM 5
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
def problem5():
    dividents = []
    numrange = 20
    for i in range(2, numrange):
        if IsPrime(0, i):
            dividents.append(i)
        else:
            for num in dividents[::-1]:
                if i%num == 0:
                    i = i/num

            if i != 1:
                dividents.append(i)

    prod = 1
    for num in dividents:
        prod = prod * num

    print "Minste positive tall som er delelig med alle tall fra 1 til", numrange, "er: \n", prod

# https://projecteuler.net/problem=6
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
def problem6():
    squareofsum = 0
    sumofsquares = 0
    naturalsum = 0
    for i in range(101):
        sumofsquares = sumofsquares + i**2
        naturalsum = naturalsum + i
    squareofsum = naturalsum**2
    result = squareofsum - sumofsquares
    print "differansen mellom square of sum og sum of squares er ", result

# https://projecteuler.net/problem=7
# primtall nummer 100001
def problem7():
    primes = [2, 3, 5]
    print(IsPrime(primes, 11))
    i = 3
    while len(primes) < 10002:
        i = i+1
        if IsPrime(primes, i):
            primes.append(i)
            print(len(primes))
    #print(primes)
    print(len(primes))
    print("primtall nummer 10001 er", primes[10000])

# https://projecteuler.net/problem=7
# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?
def problem8():
    longinteger = int("""
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450""".replace("\n", ""))
    longint_list = split_int_to_list(longinteger)
    prod = 1
    #print len(longint_list)
    maxprod = 1
    for i in range(len(longint_list)-12):
        prod = 1
        for j in range(0, 13):
            prod = prod * longint_list[i+j]
            if prod > maxprod:
                maxprod = prod
                print maxprod

# https://projecteuler.net/problem=9
def problem9():
    for i in range(1,1000):
        for j in range(i+1, 1000):
            k = ((float(i)**2+float(j)**2)**0.5)
            if k.is_integer():
                if i+j+k == 1000:
                    print("eureka")
                    print("produktet er", i*j*k)

# https://projecteuler.net/problem=10
# Find the sum of all the primes below two million.
def problem10():
    primes = [2, 3]
    iter = 0
    primelimit = 2000000
    while primes[-1] < primelimit:

        iter = iter + 1
        i = 6 * iter - 1

        if IsPrime(primes, i):
            primes.append(i)

        i = 6 * iter + 1
        if IsPrime(primes, i):
            primes.append(i)
    while primes[-1] > primelimit:
        primes.pop()

    primesum = 0

    for prime in primes:
        primesum = primesum + prime

    print "primtallsummen for primtall under", primelimit, "er:", primesum

# https://projecteuler.net/problem=11
# What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the grid?
def problem11():
    print "problem 11:"
    

    def horizontal_max(grid, line):
        multiplicatives = []
        num = grid[line][0] * grid[line][1] * grid[line][2] * grid[line][3]
        multiplicatives.append(num)  
        for i in range(len(grid[line])):
            if i > 4:
                multiplicatives.append(grid[line][i] * grid[line][i-1] * grid[line][i-2] * grid[line][i-3])
                #if grid[line][i-4] != 0:
                #    multiplicatives.append(int(multiplicatives[-1] / grid[line][i-4] * grid[line][i]))
                #else:
                #    multiplicatives.append(grid[line][i] * grid[line][i-1] * grid[line][i-2] * grid[line][i-3])


        return max(multiplicatives)

    def vertical_max(grid, line):
        grid = np.transpose(grid)
        return horizontal_max(grid, line)


    def diagnoally_max(grid):
        grid = np.array(grid)
        diags = [grid[::-1,:].diagonal(i) for i in range(-grid.shape[0]+1,grid.shape[1])]
        diags.extend(grid.diagonal(i) for i in range(grid.shape[1]-1,-grid.shape[0],-1))
        line = -1
        multiplicatives = []
        for n in diags:
            line = line + 1
            #print(n)
  
            if len(n) > 3:
                multiplicatives.append(horizontal_max(diags, line))

        return max(multiplicatives)

    grid = """
        08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
        49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
        81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
        52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
        22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
        24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
        32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
        67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
        24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
        21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
        78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
        16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
        86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
        19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
        04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
        88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
        04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
        20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
        20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
        01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
    """
    grid = [row.strip() for row in grid.split("\n")]
    grid = [[int(cell) for cell in row.split(" ")] for row in grid if row != ""]

    max_num = 0

    for i in range(len(grid[1])):
        temp_num = horizontal_max(grid,i)
        if temp_num > max_num:
            max_num = temp_num
            print(max_num)

    for i in range(len(grid[1])):
        temp_num = vertical_max(grid,i)
        if temp_num > max_num:
            max_num = temp_num
            print(max_num)


    temp_num = diagnoally_max(grid)
    if temp_num > max_num:
        max_num = temp_num
        print(max_num)


# https://projecteuler.net/problem=12
# Find triangle numbers with >500 factors
def problem12():

    #    while not num == 1:
   #         if num%divisor == 0:
  #              num = num / divisor
 #               print("num " + str(num))
#                factors = factors + 1
#            else:
#                divisor = divisor + 1
#        return factors

    numdict = {}


    def NumbersOfFactors(num):
        factors = 1



        for i in range(1, num/2 + 1):

            if num%i == 0:
                factors = factors + 1
                #if (num / i) in numdict:
                    #factors = factors + numdict[num/i]
                #    break
        #if num not in numdict:
        #    numdict[num] = factors
        #print(numdict)
        return factors

    maxFactors = 0
    seq_complete = False
    addTerm = 1
    #triangNumbers = [1]
    lastTriangleNumber = 1
    while not seq_complete:
        addTerm = addTerm + 1
        #triangNumbers.append(lastTriangleNumber + addTerm)
        lastTriangleNumber = lastTriangleNumber + addTerm
        #print("triang numbers " + str((lastTriangleNumber)))
        factors = NumbersOfFactors(lastTriangleNumber)
        if factors > maxFactors:
            print("triang numbers " + str((lastTriangleNumber)))
            maxFactors = factors
            print("max numbers of factors: " + str(maxFactors))
        #print(NumbersOfFactors(lastTriangleNumber)) 

        if factors > 500:
            seq_complete = True
    print("triang numbers " + str((lastTriangleNumber)))

    print(factors) 


# https://projecteuler.net/problem=25
# printe index med mer enn 1000 sifre
def problem25():
    prevFib = 1
    curFib = 1
    nextFib = 1

    for i in range(1000000):
        index = i + 3
        nextFib = prevFib + curFib
        prevFib = curFib
        curFib = nextFib

        if len(str(nextFib)) >= 1000:
            break
    print "fibonacci-tall med 1000 sifre har index", index

# https://projecteuler.net/problem=48
#last ten digit of self powers (1^1 + 2^2 + 3^3 + ... + 1000^1000
def problem48():
    powerRange = 1000
    sum = 0
    for pow in range(1, powerRange+1):
        temp = pow**pow
        sum = sum + temp % 10000000000
    sum = sum % 10000000000
    print sum

# https://projecteuler.net/problem=50
# Consecutive prime sum
def problem50():
    primes = [2, 3]
    #print(IsPrime(primes, 1000))
    total = 2
    iter = 0
    while primes[-1] < 1000000:
        iter = iter + 1
        i = 6 * iter - 1
        if IsPrime(primes, i):
            primes.append(i)
            total = total + 1
            #print(primes[-1])

        i = 6 * iter + 1
        if IsPrime(primes, i):
            primes.append(i)
            total = total + 1
            #print(primes[-1])

    #print(primes)
    primesum = 0
    bestCon = 0

    primecopy = primes
    addj = 2
    tempaddj = 0

    lastprime = primecopy[-1]
    primesumcopy = primecopy[:]
    primeaddjs = []


    bestCon = 0

    iterat = 0
    while primecopy:

        lastprime = primecopy[-1]

        ind = bisect.bisect_left(primecopy, lastprime/addj*3)
        primesumcopy = primecopy[:ind]
        primeaddjs = []
        primesum = 0

        while primesumcopy:

            primeaddjs = []
            primesum = 0
            tempaddj = 0
            #print(primesumcopy[:3:-1])
            for currentprime in primesumcopy[::-1]:
                primesum = primesum + currentprime
                tempaddj = tempaddj + 1
                primeaddjs.append(currentprime)

                if primesum > lastprime:
                    break
                if primesum == lastprime:
                    if addj < tempaddj:
                        print("jaddaaa. Addj: ", tempaddj)
                        print("vi traff paa ", primesum)
                        print("primes: ", primeaddjs)
                        addj = tempaddj
                        tempaddj = 0

            primesumcopy.pop()
            primesum = 0
            tempaddj = 0

        primecopy.pop()

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

# https://projecteuler.net/problem=62
# Find the smallest cube for which exactly five permutations of its digits are cube.
def problem62():
    cubelist = []
    #cube = []
    for i in range(10000):
        cube = i**3
        cubeAsList = split_int_to_list(cube)
        cubeAsList.sort()
        cubeAsIntSorted = (''.join(map(str,cubeAsList)))

        cubelist.append(cubeAsIntSorted)
    for num in cubelist:
        indices = [i for i, x in enumerate(cubelist) if x == num]
        if len(indices) == 5:
            print "hmmm.. det blir vel ", ((indices[0]**3))
            break

# https://projecteuler.net/problem=86
def problem86():

    def bestroute(l, w, h):
        lwh_list = [l, w, h]
        lwh_list.sort()
        return ((lwh_list[0]+lwh_list[1])**2+lwh_list[2]**2)**0.5

    M_limit = 1000000
    cuboid_sizes = []
    countr = 0
    countlimit = 1000000
    for l in range(1, M_limit):
        for w in range(1, l+1):
            for h in range(1, w+1):
                #res = bestroute(l,w, h)
                res = (l**2 + (w+h)**2)**0.5
                if res.is_integer():
                    countr = countr + 1
                if countr >= countlimit:
                    break
            if countr >= countlimit:
                break
        if countr >= countlimit:
            break
        if l%50 == 0:
            print "M-limit er", l
            print "Antall funn:", countr
            print "Antall funn som mangler: ", countlimit-countr

    print "Antall funn: ", countr, "tilhoerende M-limit:", l

#   https://projecteuler.net/problem=112
def problem112():

    def IsBouncy(number):
        numberList = split_int_to_list(number)
        numberListCpy = numberList[:]
        numberListCpy.sort()
        if numberList == numberListCpy or numberList == numberListCpy[::-1]:
            return False
        else:
            return True


    bouncyCounter = float(0)
    notBouncyCounter = float(0)
    for i in range(1, 11000000):
        if IsBouncy(i):
            bouncyCounter = bouncyCounter + 1
        else:
            notBouncyCounter = notBouncyCounter + 1
        if notBouncyCounter != 0 and bouncyCounter != 0:
            if (bouncyCounter / (bouncyCounter + notBouncyCounter)) >= 0.99:
                print "99 prosent ved antall", int(notBouncyCounter + bouncyCounter)
                break


def main():
    start_time = time.time()
    #problem1()
    #problem2()
    #problem3()
    #problem4()
    #problem5()
    #problem6()
    #problem7()
    #problem8()
    #problem9()
    #problem10()
    #problem11()
    #problem12()

    #problem25()
    #problem50()
    #problem48()
    #problem60()

    #problem62()

    #problem86()
    #problem112()
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()
