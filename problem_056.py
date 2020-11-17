import time

# https://projecteuler.net/problem=45
# Triangular, pentagonal, and hexagonal

def problem56():
    
    largest = 0
    for a in range(100):
        for b in range(100):
            s = 0
            n = a**b
            for el in str(n):
                s = s + int(el)
                if s > largest:
                    largest = s
    return largest
    #return (":(")



start_time = time.time()
result = problem56()

print("--- %s seconds ---" % (time.time() - start_time))
print("----------------------------------")
print("result: " + str(result))
print("----------------------------------")

