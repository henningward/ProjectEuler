import time

# https://projecteuler.net/problem=36
# Double-base palindromes

def IsPalindrome(s):
	s = str(s)
	return s == s[::-1]

def Problem36():
	result = 0
	for i in range(1000000):
		if IsPalindrome(i) and IsPalindrome("{0:b}".format(i)):
			result = result + i

	print(result)

start_time = time.time()
Problem36()
print("--- %s seconds ---" % (time.time() - start_time))