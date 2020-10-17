# https://projecteuler.net/problem=9
def problem9():
    for i in range(1,1000):
        for j in range(i+1, 1000):
            k = ((float(i)**2+float(j)**2)**0.5)
            if k.is_integer():
                if i+j+k == 1000:
                    print("eureka")
                    print("produktet er", i*j*k)


problem9()