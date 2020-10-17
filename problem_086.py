# https://projecteuler.net/problem=86
def problem86():

    def bestroute(l, w, h):
        lwh_list = [l, w, h]
        lwh_list.sort()
        return ((lwh_list[0]+lwh_list[1])**2+lwh_list[2]**2)**0.5

    M_limit = 1000000
    cuboid_sizes = []
    countr = 0
    countlimit = 1000000
    for l in range(1, M_limit):
        for w in range(1, l+1):
            for h in range(1, w+1):
                #res = bestroute(l,w, h)
                res = (l**2 + (w+h)**2)**0.5
                if res.is_integer():
                    countr = countr + 1
                if countr >= countlimit:
                    break
            if countr >= countlimit:
                break
        if countr >= countlimit:
            break
        if l%50 == 0:
            print "M-limit er", l
            print "Antall funn:", countr
            print "Antall funn som mangler: ", countlimit-countr

    print "Antall funn: ", countr, "tilhoerende M-limit:", l

problem86()