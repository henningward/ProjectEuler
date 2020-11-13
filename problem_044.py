import time

# https://projecteuler.net/problem=44
# Pentagon numbers

def binarySearch(arr, l, r, x):
    # Check base case
    if r >= l:

        mid = int(l + (r - l) / 2)

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

            # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)

            # Else the element can only be present in right subarray
        else:
            return binarySearch(arr, mid + 1, r, x)

    else:
        # Element is not present in the array
        return -1


def Pentagon(n):
    return int(n * (3 * n - 1) / 2)

def problem44():
    pentagonList = []
    for i in range(1, 3000):
        pentagonList.append(Pentagon(i))
    D_min = 99999999

    for i in range(1, 3000):
        if i%100 == 0:
            print(i)
        for j in range(i+1, 3000):

            s1 = binarySearch(pentagonList, 0, len(pentagonList) - 1, Pentagon(j) + Pentagon(i) )
            s2 = binarySearch(pentagonList, 0, len(pentagonList) - 1, Pentagon(j) - Pentagon(i) )
            if s1 is not -1 and s2 is not -1:
                D = Pentagon(j) - Pentagon(i) 
                print(D)
                if (D < D_min):
                    D_min = D
                    print(D_min)
                    
    print(D_min)



start_time = time.time()
problem44()
print("--- %s seconds ---" % (time.time() - start_time))