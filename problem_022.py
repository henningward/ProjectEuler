import time

# https://projecteuler.net/problem=22
# Names scores

def CalculateNameValue(name):
	result = 0
	for letter in name:

		result = result + ord(letter.lower()) - 96
	return result


def problem22():
	f = open("problem_022.txt", "r")
	names = f.read()
	names = [name[1:-1] for name in sorted(names.split(","))]

	itr = 0
	totalScore = 0
	for name in names:
		itr = itr + 1
		totalScore = totalScore + itr * CalculateNameValue(name)
	print(totalScore)


start_time = time.time()
problem22()
print("--- %s seconds ---" % (time.time() - start_time))

