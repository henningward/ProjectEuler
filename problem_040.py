import time

# https://projecteuler.net/problem=40
# Champernowne's constant

def problem40():
    index = 0
    scale = 1
    result = 1
    for i in range(1, 1000000):

        for elem in str(i):
            index = index + 1
            
            if (index%scale == 0):
                scale = scale * 10
                result = result * int(elem)
                #print(index, elem)
            

    print(result)

start_time = time.time()
problem40()
print("--- %s seconds ---" % (time.time() - start_time))