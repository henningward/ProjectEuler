# PROBLEM 5
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
def problem5():
    dividents = []
    numrange = 20
    for i in range(2, numrange):
        if IsPrime(0, i):
            dividents.append(i)
        else:
            for num in dividents[::-1]:
                if i%num == 0:
                    i = i/num

            if i != 1:
                dividents.append(i)

    prod = 1
    for num in dividents:
        prod = prod * num

    print "Minste positive tall som er delelig med alle tall fra 1 til", numrange, "er: \n", prod


    problem5()