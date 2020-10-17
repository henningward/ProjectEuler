# PROBLEM 4
# Find the largest palindrome made from the product of two 3-digit numbers.

def split_int_to_list(word):
    listofints = []
    listofstrings = [char for char in str(word)]
    for i in range(0, len(listofstrings)):
        listofints.append(int(listofstrings[i]))
    return listofints


def problem4():
    products = []
    for i in range(100, 1000):
        for j in range(100, 1000):
            products.append(i*j)
    products.sort()
    for integ in products[::-1]:
        tempInt = split_int_to_list(integ)
        tempIntRev = tempInt[::-1]
        if tempInt == tempIntRev:
            print "storste palindrome-produkt er", ''.join(map(str, tempIntRev))
            break

problem4()