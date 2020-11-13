import time
import math
# https://projecteuler.net/problem=61
# Cyclical figurate numbers

def Triangle(n): return int(n * (n + 1) / 2)
def Pentagonal(n): return int(n * (3 * n - 1) / 2)
def Hexagonal(n): return int(n * (2 * n - 1))

def IsPentagonal(n): return ((1/3 + math.sqrt(1/9 + 4 * 2/3 * n))/2).is_integer() or ((1/3 - math.sqrt(1/9 + 4 * 2/3 * n))/2).is_integer() 
def IsHexagonal(n): return ((1/2 + math.sqrt(1/4 + 2 * n))/2).is_integer() or ((1/3 - math.sqrt(1/4 + 2 * n))/2).is_integer() 

def P(order, n):
    if order == 3:
        return int(n * (n + 1) / 2)
    if order == 4:
        return int(n**2)
    if order == 5:
        return int(n * (3 * n - 1) / 2)
    if order == 6:
        return int(n * (2 * n - 1))
    if order == 7:
        return int(n * (5 * n - 3)/2)
    if order == 8:
        return int(n * (3 * n - 2))

def NextCycle(p, num):
    if p == 6:

        return True
    nxt = str(num)[len(str(num)) -2:]
    for i in range(1,150):
        num = P(p, i)
        if len(str(num)) == 4:

            if int(str(num)[:2]) == int(nxt):

                NextCycle(p+1, num)
    return False

def problem61():

#PROBLEM: p3 trenger ikke være etterfulgt av p4 osv.. 

    success = False
    #while not success:
    for i in range(1,150):
        num = P(3, i)
        if len(str(num)) == 4:
            
            success =  NextCycle(5, num)
            if success == True:
                return success
        
    
    return (":(")

start_time = time.time()
result = problem61()

print("--- %s seconds ---" % (time.time() - start_time))
print("----------------------------------")
print("result: " + str(result))
print("----------------------------------")

