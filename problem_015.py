import time
import numpy as np

# https://projecteuler.net/problem=15
# Lattice paths
def problem15():
	gridsize = 21
	grid = np.zeros(shape=(gridsize,gridsize))

	for i in range(gridsize):
		grid[gridsize-1][i] = 1
		grid[i][gridsize-1] = 1
	#print grid

	for i in range(gridsize-2, -1, -1):
		for j in range(gridsize-2, -1, -1):
			grid[i][j] = grid[i+1][j] + grid[i][j+1]
	#print(grid)

	print(grid[0][0])

start_time = time.time()
problem15()
print("--- %s seconds ---" % (time.time() - start_time))

