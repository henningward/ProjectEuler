import time
import math
# https://projecteuler.net/problem=45
# Goldbach's other conjecture

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

def Squares(n):
    squares = []
    for i in range(int(math.sqrt(n)) + 3):
        squares.append(i**2)
    return squares

def problem46():
    smallest = 9999999
    for i in range(2, 300):
        for j in range(i, 300):
            valid = False
            composite = i * j
            if composite%2 is not 0:
                for square in Squares(composite):
                    if IsPrime(composite - 2*square):
                        valid = True
                if not valid:
                    if composite < smallest:
                            smallest = composite
    return smallest

start_time = time.time()
result = problem46()

print("--- %s seconds ---" % (time.time() - start_time))

print("result: " + str(result))
