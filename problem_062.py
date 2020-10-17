
def split_int_to_list(word):
    listofints = []
    listofstrings = [char for char in str(word)]
    for i in range(0, len(listofstrings)):
        listofints.append(int(listofstrings[i]))
    return listofints

# https://projecteuler.net/problem=62
# Find the smallest cube for which exactly five permutations of its digits are cube.
def problem62():
    cubelist = []
    #cube = []
    for i in range(10000):
        cube = i**3
        cubeAsList = split_int_to_list(cube)
        cubeAsList.sort()
        cubeAsIntSorted = (''.join(map(str,cubeAsList)))

        cubelist.append(cubeAsIntSorted)
    for num in cubelist:
        indices = [i for i, x in enumerate(cubelist) if x == num]
        if len(indices) == 5:
            print "hmmm.. det blir vel ", ((indices[0]**3))
            break

problem62()