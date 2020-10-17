def split_int_to_list(word):
    listofints = []
    listofstrings = [char for char in str(word)]
    for i in range(0, len(listofstrings)):
        listofints.append(int(listofstrings[i]))
    return listofints   

#   https://projecteuler.net/problem=112
def problem112():

    def IsBouncy(number):
        numberList = split_int_to_list(number)
        numberListCpy = numberList[:]
        numberListCpy.sort()
        if numberList == numberListCpy or numberList == numberListCpy[::-1]:
            return False
        else:
            return True


    bouncyCounter = float(0)
    notBouncyCounter = float(0)
    for i in range(1, 11000000):
        if IsBouncy(i):
            bouncyCounter = bouncyCounter + 1
        else:
            notBouncyCounter = notBouncyCounter + 1
        if notBouncyCounter != 0 and bouncyCounter != 0:
            if (bouncyCounter / (bouncyCounter + notBouncyCounter)) >= 0.99:
                print "99 prosent ved antall", int(notBouncyCounter + bouncyCounter)
                break

problem112()