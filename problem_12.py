# https://projecteuler.net/problem=12
# Find triangle numbers with >500 factors
def problem12():

    #    while not num == 1:
   #         if num%divisor == 0:
  #              num = num / divisor
 #               print("num " + str(num))
#                factors = factors + 1
#            else:
#                divisor = divisor + 1
#        return factors

    numdict = {}


    def NumbersOfFactors(num):
        factors = 1



        for i in range(1, num/2 + 1):

            if num%i == 0:
                factors = factors + 1
                #if (num / i) in numdict:
                    #factors = factors + numdict[num/i]
                #    break
        #if num not in numdict:
        #    numdict[num] = factors
        #print(numdict)
        return factors

    maxFactors = 0
    seq_complete = False
    addTerm = 1
    #triangNumbers = [1]
    lastTriangleNumber = 1
    while not seq_complete:
        addTerm = addTerm + 1
        #triangNumbers.append(lastTriangleNumber + addTerm)
        lastTriangleNumber = lastTriangleNumber + addTerm
        #print("triang numbers " + str((lastTriangleNumber)))
        factors = NumbersOfFactors(lastTriangleNumber)
        if factors > maxFactors:
            print("triang numbers " + str((lastTriangleNumber)))
            maxFactors = factors
            print("max numbers of factors: " + str(maxFactors))
        #print(NumbersOfFactors(lastTriangleNumber)) 

        if factors > 500:
            seq_complete = True
    print("triang numbers " + str((lastTriangleNumber)))

    print(factors) 

problem12()