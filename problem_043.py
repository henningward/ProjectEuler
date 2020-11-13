import time
import itertools

# https://projecteuler.net/problem=43
# Sub-string divisibility

def split_int_to_list(word):
    listofints = []
    listofstrings = [char for char in str(word)]
    for i in range(0, len(listofstrings)):
        listofints.append(int(listofstrings[i]))
    return listofints

def listToInt(n):
    return int(''.join(map(str,n)))


def NewPermutations(notToBeIncluded, length):
    substr = ""
    for i in range(10):
        if str(i) not in str(notToBeIncluded):
            substr = substr + str(i)

    temp = list(itertools.permutations(split_int_to_list(substr), length))
    triplePermutations = []
    for combination in temp:
        triplePermutations.append(listToInt(combination))

    return triplePermutations

def problem43():

    d6d7d8 = []
    comb = NewPermutations(5, 2)
    for n in comb:
        if len(str(n)) is not 2:
            n = str(0) + str(n)
        if int(str(5) + str(n)) % 11 == 0:
            #print(str(5) + str(n))
            d6d7d8.append((str(5) + str(n)))

    d7d8 = [(n[1:]) for n in d6d7d8]

    d6d7d8d9 = []

    for n in d7d8:
        d9 = NewPermutations(int(str(5) + str(n)), 1)

        for d in d9:
            if int(str(n) + str(d)) % 13 == 0:
                d6d7d8d9.append(str(5) + str(n) + str(d))

    d6d7d8d9d10 = []

    for n in d6d7d8d9:
        nsliced = n[2:]
        d10 = NewPermutations(int(str(5) + str(nsliced)), 1)

        for d in d10:
            if int(str(nsliced) + str(d)) % 17 == 0:
                d6d7d8d9d10.append(str(n) + str(d))
    
    d5d6d7d8d9d10 = []

    for n in d6d7d8d9d10:
        d6d7 = n[:2]
        d5 = NewPermutations(int(d6d7), 1)

        for d in d5:
            if int(str(d) + str(d6d7)) % 7 == 0:
                d5d6d7d8d9d10.append(str(d) + str(n))

    d3d4d5d6d7d8d9d10 = []

    for n in d5d6d7d8d9d10:

        d3d4 = NewPermutations(int(n), 2)
        d5 = str(n)[0]
        for d in d3d4:
            if len(str(d)) is not 2:
                d = str(0) + str(d)
            d4 = str(d)[1]
            if int(str(d) + str(d5)) % 3 == 0:                    
                if int(d4) % 2 == 0:
                    d3d4d5d6d7d8d9d10.append(str(d) + str(n))

    d1d2d3d4d5d6d7d8d9d10 = []

    for n in d3d4d5d6d7d8d9d10:
        if str(0) in n:
            d1d2 = NewPermutations(int(n + str(0)), 2)
        else:
            d1d2 = NewPermutations(int(n), 2)
        for d in d1d2:
            d1d2d3d4d5d6d7d8d9d10.append(int(str(d) + str(n)))
    return sum(d1d2d3d4d5d6d7d8d9d10)
    print("result: " + str(sum(d1d2d3d4d5d6d7d8d9d10)))

start_time = time.time()
result = problem43()

print("--- %s seconds ---" % (time.time() - start_time))

print("result: " + str(result))