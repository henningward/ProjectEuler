import time
import itertools
# https://projecteuler.net/problem=24
# Lexicographic permutations

def problem24():
	numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	print(list(itertools.permutations(numbers, 10))[999999])




start_time = time.time()
problem24()
print("--- %s seconds ---" % (time.time() - start_time))