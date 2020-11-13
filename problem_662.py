import time
import math
import numpy as np
import pylab as plt

# https://projecteuler.net/problem=662
# Fibonacci paths


def Fibonacci():
    prevFib = 1
    curFib = 1
    nextFib = 1

    result = [1]
    for i in range(10000):
        nextFib = prevFib + curFib
        prevFib = curFib
        curFib = nextFib
        if nextFib >= 10000:
            break
        result.append(nextFib)
    
    return result


def PopulateGrid(grid, fib, xpos, ypos, N, M):

    for i in range(0, N-xpos):  
        for j in range(0, M-ypos):
            dist = math.sqrt(i**2 + j**2)
            if dist.is_integer() and int(dist) in fib:
                grid[xpos+i][ypos+j] += grid[xpos][ypos]
    return grid

def PopulateGridEfficient(grid, steps, xpos, ypos, N, M):
    for step in steps:
        if xpos+step[0] < N and ypos+step[1] < M:
            grid[xpos+step[0]][ypos+step[1]] += (grid[xpos][ypos] % 10000000000)
    return grid

def GetAllRightAngleSteps(c):
    # a^2 + b^2 = c^2 
    result = []
    for a in range(0, c+1):
        b = math.sqrt(c**2 - a**2)
        if (b.is_integer()):
            result.append([a, int(b)])
            #result.append([int(b), a])
    return result

def GetAllRightAngleSteps2(steps, c):

    for a in range(0, c+1):
        b = math.sqrt(c**2 - a**2)
        if (b.is_integer()):
            steps.append([a, int(b)])
            

def Problem662():

    #print (519145470394 % 1000000007)
    fib = Fibonacci()
    steps = []
    for f in fib:
        GetAllRightAngleSteps2(steps, f)
    #print(steps)

    #print(fib)

    N = 10
    M = 10

    N = N + 1
    M = M + 1
    grid = np.zeros((N, M))
    grid[0][0] = 1
    xpos = 0
    ypos = 0



    for i in range(N):
        if (i%(int(N/100)+1) == 0):
            pct = (i+1) / N * 100
            print(str(int(pct)) + " percent done")

        for j in range(M):
            if grid[i][j]:
                PopulateGridEfficient(grid, steps, i, j, N, M)
                #a = 2
                #PopulateGrid(grid, fib, i, j, N, M)


    print(grid[N-1][M-1])

    grid[grid==0] = None

    grid2 = np.zeros((N, M))
    grid2[0][0] = 1
    #PopulateGrid(grid2, fib, xpos, ypos, N, M)
    grid2[grid2==0] = None

    pwargs = {'interpolation':'nearest'}
    #plt.imshow(grid,cmap=plt.cm.hsv,origin='lower', **pwargs)
    plt.imshow(grid2,cmap=plt.cm.jet, origin='lower', **pwargs)
    #plt.imshow(grid, origin='lower')
    #plt.imshow(grid2, origin='lower')
    
    #plt.show()

    return 0

start_time = time.time()
Problem662()
print("--- %s seconds ---" % (time.time() - start_time))