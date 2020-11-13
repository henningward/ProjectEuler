import time
import math
# https://projecteuler.net/problem=45
# Triangular, pentagonal, and hexagonal

def Triangle(n): return int(n * (n + 1) / 2)
def Pentagonal(n): return int(n * (3 * n - 1) / 2)
def Hexagonal(n): return int(n * (2 * n - 1))

def IsPentagonal(n): return ((1/3 + math.sqrt(1/9 + 4 * 2/3 * n))/2).is_integer() or ((1/3 - math.sqrt(1/9 + 4 * 2/3 * n))/2).is_integer() 
def IsHexagonal(n): return ((1/2 + math.sqrt(1/4 + 2 * n))/2).is_integer() or ((1/3 - math.sqrt(1/4 + 2 * n))/2).is_integer() 

def CheckIfPentOrHex(n):
    pent = False
    hexa = False
    for i in range(1000000):
        if Pentagonal(i) == n:
            pent = True
        if Hexagonal(i) == n:
            hexa = True
        if (Pentagonal(i) > n and pent is not True) or (Hexagonal(i) > n and hexa is not True):
            return False
        if pent == True and hexa == True:
            return True
    return False
            
def problem45():
    #for i in range(700):
        #print(Pentagonal(i))
        # 567645
    for n in range(1000, 5000000):
        tri = Triangle(n)
        if IsPentagonal(tri) and IsHexagonal(tri):
            if CheckIfPentOrHex(tri):
                return tri
    return 0

start_time = time.time()
result = problem45()
print("--- %s seconds ---" % (time.time() - start_time))
print("result: " + str(result))