def gcd(m,n):
    cf = []
    for i in range(1,min(m,n)+1):
        if (m % i) == 0 and (n % i) == 0:
            mrcf = i
    return mrcf


print(gcd(12,16))