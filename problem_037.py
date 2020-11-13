import time

# https://projecteuler.net/problem=37
# Double-base palindromes


def split_int_to_list(word):
    listofints = []
    listofstrings = [char for char in str(word)]
    for i in range(0, len(listofstrings)):
        listofints.append(int(listofstrings[i]))
    return listofints

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

def IsTrunctedPrime(value):
	if not IsPrime(value):
		return False
	truncted1 = str(value)
	truncted2 = str(value)
	for k in range(len(str(value))-1):
		truncted1 = ((truncted1)[1:])
		if not IsPrime(int(truncted1)):
			return False
		truncted2 = ((truncted2)[:-1])
		if not IsPrime(int(truncted2)):
			return False
	return True

def Problem37():
	sum = 0
	for i in range(10, 1000000):
		if (IsTrunctedPrime(i)):
			sum = sum + i

	print(sum)



start_time = time.time()
Problem37()
print("--- %s seconds ---" % (time.time() - start_time))