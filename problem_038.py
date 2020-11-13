import time

# https://projecteuler.net/problem=37
# Double-base palindromes


def split_int_to_list(word):
    listofints = []
    listofstrings = [char for char in str(word)]
    for i in range(0, len(listofstrings)):
        listofints.append(int(listofstrings[i]))
    return listofints

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
  
def PanDigital(num, n):

    result = ""
    for i in range(1, n + 1):
        result += str(num * i)
        if (len(result) > 9):
            return -1

    return int(result)

def Problem38():

    alltimeBest = 0
    bestN = 0


    #Prøve n = 2
    for n in range(2, 3):
        score = 0
        num = 1
        while score >= 0:
            num+=1
            score = PanDigital(num, n)

            if score > alltimeBest and isUniqueChars(str(score)) and "0" not in str(score):
                alltimeBest = score
                bestN = n

    print(alltimeBest)
    print(bestN)
    #print(PanDigital(192, 3))



start_time = time.time()
Problem38()
print("--- %s seconds ---" % (time.time() - start_time))