import time
from fractions import Fraction
# https://projecteuler.net/problem=33
# Digit cancelling fractions

def problem33():
	product = 1
	for i in range(11, 100):
		for j in range(i, 100):
			nom1 = int(str(i)[0])
			nom2 = int(str(i)[-1])
			den1 = int(str(j)[0])
			den2 = int(str(j)[-1])
			if i%10!=0 and j%10!=0:	
				if nom1 is not nom2 and den1 is not den2:
					if nom1 == den2 or nom2 == den1:
						if (nom1 / den2 == i /j) or (nom2 / den1 == i / j):
							product = product * i / j
	print(product)
				
start_time = time.time()
problem33()
print("--- %s seconds ---" % (time.time() - start_time))
